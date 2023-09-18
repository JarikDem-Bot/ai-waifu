<h1 align="center"> AI Waifu (VTuber) </h1>

<div align="center">
  
<a href="/LICENSE">![GitHub](https://img.shields.io/github/license/JarikDem-Bot/ai-waifu-test)</a>
<a href="">![GitHub top language](https://img.shields.io/github/languages/top/JarikDem-Bot/ai-waifu-test)</a>
<a href="">![Static Badge](https://img.shields.io/badge/Anime%20-%20AI%20waifu%20-%20lightpink)</a>

</div>

**Anime AI Waifu** is an AI powered voice assistant with VTuber's model, that combines the charm of anime characters with cutting-edge technologies. This project is meant to create an engaging experience where you can interact with desired character in real-time without powerful hardware.


## Features

- 🎤 **Voice Interaction:** Speak to your AI waifu and get instant (almost) responses.
    - Whisper - openai's paid speech recognition.
    - Google sr - free speech recognition alternative.
    - Console - if you don't want use microphone just type prompts with your keyboard.

- 🤖 **AI Chatbot Integration:** Conversations are powered by an AI chatbot, ensuring engaging and dynamic interactions.
    - Openai's *'gpt-3.5-turbo'* or any other available model.
    - File with personality and behaviour description.
    - Remembers previous messages.

- 📢 **Text-to-Speech:** Hear your AI waifu's responses as she speaks back to you, creating an immersive experience.
    - Google tts - free and simple solution.
    - ElevenLabs - amazing results, tons of voices.
    - Console - get text responses in your console (but VTube model will be just idle).

- 🌐 **Integration with VTube Studio:** Seamlessly connect your AI waifu to VTube Studio for an even more lifelike and visually engaging interaction.
    - Lipsync while talking.


## Showcase

[![Video demonstration](https://i.ibb.co/zm42TCq/2023-08-23-104833.png)](https://youtu.be/e8sF09jf_DA)

*Demonstration in real time without cutouts or speed up. This is real delay in answers.

## Installation

To run this project, you need:
 1. Install Python 3.10.5 if you don't already have it installed.
 2. Clone the repository by running `git clone https://github.com/JarikDem-Bot/ai-waifu.git`
 3. Install the required Python packages by running `pip install -r requirements.txt` in the project directory.
 4. Create `.env` file inside the project directory and enter your API keys
    <details>
      <summary> .env template</summary>
      
      ```shell
      OPENAI_API_KEY='YOUR_OPEN_AI_KEY'
      ELEVENLABS_API_KEY='YOUR_ELEVENLABS_KEY'
      ```
    </details>
    
 5. Install [VB-Cable](https://vb-audio.com/Cable/)
 7. Install and set [VTube Studio](https://store.steampowered.com/app/1325860/VTube_Studio/)
    <details>
      <summary>Settings: </summary>
      
      - Select `CABLE Output` as microphone. Select `Preview microphone audio` to hear waifu's answers

        <img src='https://github.com/JarikDem-Bot/ai-waifu/assets/73791422/a38f8b45-44f3-4b4d-9626-2f3c812b8ba2' width='50%'>
        
      - Select input and output for `Mouth Open`. Optionally you can set "breathing" to get idle movents.

        <img src='https://github.com/JarikDem-Bot/ai-waifu/assets/73791422/4e7341b1-91a8-48f9-94e4-b5669163c89b' width='50%'>

    </details>


 9. Select your required settings in `main.py` in `waifu.initialize`
     <details>
      <summary>Arguments: </summary>
      
      - `user_input_service` (str) - the way to interact with Waifu
          - `"whisper"` - OpenAI's whisper speech to text service; paid, requires OpanAi API key.
          - `"google"` - free google speech to text service.
          - `"console"` - type your promt in console with text (absoulutely free).
          - `None` or unspecified - default value is `"whisper"`.
      - `stt_duration` (float) - the maximum number of seconds that it will dynamically adjust the threshold for before returning. This value should be at least 0.5 in order to get a representative sample of the ambient noise. Default value is `0.5`.
      - `mic_index` (int) - index of the device to use for audio input. If `None` or unspecified will use default microphone.

      - `chatbot_service` (str) - service that will generate responses
          - `"openai"` - OpenAI text generation servise; paid, requires OpanAi API key.
          - `"test"` - returns prewritten message; used as dummy text for developement to reduce time and cost of testings.
          - `None` or unspecified - default value is `"openai"`.
      - `chatbot_model` (str) - model used for text generation. List of available models you can find [here](https://platform.openai.com/docs/models/overview). Default value is `"gpt-3.5-turbo"`.
      - `chatbot_temperature` (float) - determines creativity of the generated text. A higher value leads to more creative result. A lower value leads to less creative and more similar results. Default value is `0.5`.
      - `personality_file` (str) - relative path to txt file with waifu's description. Default value is `"personality.txt"`.
        
      - `tts_service` (str) - service that "reads" Waifu's responses
          - `"google"` - free Google's tts, voice feels very "robotic".
          - `"elevenlabs"` - ElevenLabs tts with good quality; paid, requires ElevenLabs API key.
          - `"console"` - output will be printed in console (free).
          - `None` or unspecified - default value is `"google"`.
      - `output_device` - (int) output device ID or (str) output device name substring. If VB-Cable is used, you need to find device, that will start with `CABLE Input (VB-Audio Virtual` using `sd.query_devices()` command. 
      - `tts_voice` (str) - ElevenLabs voice name. Default value is `"Elli"`.
      - `tts_model` (str) - ElevenLabs model. Recommended values are `"eleven_monolingual_v1"` and `"eleven_multilingual_v1"`. Default value is `"eleven_monolingual_v1"`.

    </details>

    
 10. Run the project by executing `python main.py` in the project directory.

<br>

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/warning.svg">
> </picture><br>
>
> Depending on the selected input mode, program may send all recorded sounds or other data to the 3-rd parties such as: Google (stt, tts), OpenAI (stt, text generation), ElevenLabs (tts).


## License

[MIT](/LICENSE)
