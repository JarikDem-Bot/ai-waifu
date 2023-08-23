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

 1. Install Python 3.10.5 if you don't already have it installed.
 2. Clone the repository by running `git clone https://github.com/JarikDem-Bot/ai-waifu.git`
 3. Install the required Python packages by running `pip install -r requirements.txt` in the project directory.
 4. Create `.env` file and enter your API keys
    <details>
      <summary> .env template</summary>
      
      ```shell
      VTS_TOKEN=''
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


 9. Select your required settings in `main.py` in `waifu.initialise`
 10. Run the project by executing `python main.py` in the project directory.

<br>

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/warning.svg">
> </picture><br>
>
> Depending on the selected input mode, program may send all recorded sounds to the 3-rd parties.


## License

[MIT](/LICENSE)
