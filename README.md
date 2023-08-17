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
    - ElevenLabs - **_in progress..._**
    - Console - get text responses in your console (but VTube model will be just idle).

- 🌐 **Integration with VTube Studio:** Seamlessly connect your AI waifu to VTube Studio for an even more lifelike and visually engaging interaction.
    - Lipsync while talking.


## Showcase

_Here will be video/gif demonstration of this project :3_


## Installation

Here are the steps to get started:

 1. Install Python 3.10.5 if you don't already have it installed.
 2. Clone the repository by running `git clone https://github.com/JarikDem-Bot/ai-waifu.git`
 3. Install the required Python packages by running `pip install -r requirements.txt` in the project directory.
 4. Create `.env` file and enter your API keys
    <details>
      <summary> .env template</summary>
      
      ```
      VTS_TOKEN=''
      OPENAI_API_KEY='YOUR_OPEN_AI_KEY'
      ```
    </details>
    
 5. Install [VB-Cable](https://vb-audio.com/Cable/)
 6. Select your required settings in `main.py` in `waifu.initialise`
 7. Run the project by executing `python main.py` in the project directory.

<br>

> <picture>
>   <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/light-theme/warning.svg">
>   <img alt="Warning" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/warning.svg">
> </picture><br>
>
> Depending on the selected input mode, program may send all recorded sounds to the 3-rd parties.


## License

[MIT](/LICENSE)
