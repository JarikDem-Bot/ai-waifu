from waifu import Waifu

def main():
    waifu = Waifu()

    waifu.initialise(user_input_service='whisper',
                 chatbot_service='openai',
                 tts_service='google', output_device=8)

    while True:
        waifu.conversation_cycle()

if __name__ == "__main__":
    main()