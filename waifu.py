import openai
import speech_recognition as sr
from gtts import gTTS
import sounddevice as sd
import soundfile as sf

from dotenv import load_dotenv
from os import getenv, path
from json import load, dump

class Waifu:
    def __init__(self) -> None:
        self.mic = None
        self.recogniser = None

        self.user_input_service = None
        self.stt_duration = None

        self.chatbot_service = None
        self.chatbot_model = None
        self.chatbot_temperature = None
        self.chatbot_personality_file = None

        self.message_history = []
        self.context = []

        self.tts_service = None


    def initialise(self, user_input_service:str | None = None, stt_duration:float | None = None, mic_index:int | None = None,
                    chatbot_service:str | None = None, chatbot_model:str | None = None, chatbot_temperature:float | None = None, personality_file:str | None = None,
                    tts_service:str | None = None, output_device = None) -> None:
        load_dotenv()

        self.update_user_input(user_input_service=user_input_service, stt_duration=stt_duration)
        self.mic = sr.Microphone(device_index=mic_index)
        self.recogniser = sr.Recognizer()
        
        openai.api_key = getenv("OPENAI_API_KEY")
        self.update_chatbot(service = chatbot_service, model = chatbot_model, temperature = chatbot_temperature, personality_file = personality_file)
        self.__load_chatbot_data()

        self.update_tts(service=tts_service, output_device=output_device)

    def update_user_input(self, user_input_service:str | None = 'whisper', stt_duration:float | None = 0.5) -> None:
        if user_input_service:
            self.user_input_service = user_input_service
        elif self.user_input_service is None:
            self.user_input_service = 'whisper'

        if stt_duration:
            self.stt_duration = stt_duration
        elif self.stt_duration is None:
            self.stt_duration = 0.5

    def update_chatbot(self, service:str | None = 'openai', model:str | None = 'gpt-3.5-turbo', temperature:float | None = 0.5, personality_file:str | None = 'personality.txt') -> None:
        if service:
            self.chatbot_service = service
        elif self.chatbot_service is None:
            self.chatbot_service = 'openai'

        if model:
            self.chatbot_model = model
        elif self.chatbot_model is None:
            self.chatbot_model = 'gpt-3.5-turbo'

        if temperature:
            self.chatbot_temperature = temperature
        elif self.chatbot_temperature is None:
            self.chatbot_temperature = 0.5

        if personality_file:
            self.chatbot_personality_file = personality_file
        elif self.chatbot_personality_file is None:
            self.chatbot_personality_file = 'personality.txt'

    def update_tts(self, service:str | None = 'google', output_device = None) -> None:
        if service:
            self.tts_service = service
        elif self.tts_service is None:
            self.tts_service = 'google'

        if output_device is not None:
            sd.check_output_settings(output_device)
            sd.default.samplerate = 44100
            sd.default.device = output_device

    def get_audio_devices(self):
        return sd.query_devices()

    def get_user_input(self, service:str | None = None, stt_duration:float | None = None) -> str:
        service = self.user_input_service if service is None else service
        stt_duration = self.stt_duration if stt_duration is None else stt_duration

        supported_stt_services = ['whisper', 'google']
        supported_text_services = ['console']

        result = ""
        if service in supported_stt_services:
            result = self.__recognise_speech(service, duration=stt_duration)
        elif service in supported_text_services:
            result = self.__get_text_input(service)
        else:
            raise ValueError(f"{service} servise doesn't supported. Please, use one of the following services: {supported_stt_services + supported_text_services}")
        
        return result

    def get_chatbot_response(self, prompt:str, service:str | None = None, model:str | None = None, temperature:float | None = None) -> str:
        service = self.chatbot_service if service is None else service
        model = self.chatbot_model if model is None else model
        temperature = self.chatbot_temperature if temperature is None else temperature

        supported_chatbot_services = ['openai', 'test']

        result = ""
        if service == 'openai':
            result = self.__get_openai_response(prompt, model=model, temperature=temperature)
        elif service == 'test':
            result = "This is test answer from Waifu. Nya kawaii, senpai!"
        else:
            raise ValueError(f"{service} servise doesn't supported. Please, use one of the following services: {supported_chatbot_services}")
        
        return result

    def tts_say(self, text:str, service:str | None = None, voice:str | None = None) -> None:
        service = self.tts_service if service is None else service

        supported_tts_services = ['google', 'elevenlabs', 'console']

        if service not  in supported_tts_services:
            raise ValueError(f"{service} servise doesn't supported. Please, use one of the following services: {supported_tts_services}")
        


        if service == 'google':
            gTTS(text=text, lang='en', slow=False, lang_check=False).save('output.mp3')

            data, fs = sf.read('output.mp3')
            sd.play(data, fs)
            sd.wait()
        elif service == 'elevenlabs':
            pass
        elif service == 'console':
            print('\n\33[7m' + "Waifu:" + '\33[0m' + f' {text}')

    def conversation_cycle(self) -> dict:
        input = self.get_user_input()

        response = self.get_chatbot_response(input)

        self.tts_say(response)
        
        return dict(user = input, assistant = response)

    def __get_openai_response(self, prompt:str, model:str, temperature:float) -> str:
        self.__add_message('user', prompt)
        messages = self.context + self.message_history

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, 
        )
        response = response.choices[0].message["content"]

        self.__add_message('assistant', response)
        self.__update_message_history()

        return response

    def __add_message(self, role:str, content:str) -> None:
        self.message_history.append({'role': role, 'content': content})

    def __load_chatbot_data(self, file_name:str | None = None) -> None:
        file_name = self.chatbot_personality_file if file_name is None else file_name

        with open(file_name, 'r') as f:
            personality = f.read()
        self.context = [{'role': 'system', 'content': personality}]

        if path.isfile('./message_history.txt'):
            with open('message_history.txt', 'r') as f:
                self.message_history = load(f)

    def __update_message_history(self) -> None:
        with open('message_history.txt', 'w') as f:
                dump(self.message_history, f)

    def __get_text_input(self, service:str) -> str:
        user_input = ""
        if service == 'console':
            user_input = input('\n\33[42m' + "User:" + '\33[0m' + " ")
        return user_input

    def __recognise_speech(self, service:str, duration:float) -> str:
        with self.mic as source:
            print('(Start listening)')
            self.recogniser.adjust_for_ambient_noise(source, duration=duration)
            audio = self.recogniser.listen(source)
            print('(Stop listening)')

            result = ""
            try:
                if service == 'whisper':
                    result = self.__whisper_sr(audio)
                elif service == 'google':
                    result = self.recogniser.recognize_google(audio)
            except Exception as e:
                print(f"Exeption: {e}")
        return result

    def __whisper_sr(self, audio) -> str:
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
            audio_file = open('speech.wav', 'rb')
            transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file)
        return transcript['text']



def main():
    w = Waifu()
    w.initialise(user_input_service='console', 
                 chatbot_service='test', 
                 tts_service='google', output_device=8)

    while True:
        w.conversation_cycle()

if __name__ == "__main__":
    main()