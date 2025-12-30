import random

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️ file not found. Run: pip install pyttsx3; in the terminal")

def setup_tts():
    if not TTS_AVAILABLE:
        return None
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)
        return engine
    except:
        return None
    
def speak(engine, text):
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            print(f"🔇 [AUDIO]: {text}")
    
    else:
        print(f"🔇 [AUDIO] : {text}")

def get_samples():
    return[
        "Hello",
        "Good morning",
        "How are you",
        "Have a nice day"
    ]

def main():
    print("🤖 AI VOICE LAB")
    print("=============================================")

    engine = setup_tts()

    if engine:
        print("✅ Voice ready! Try typing something...")

    else:
        print("⚠️ No audio")

    speak(engine, "Hello! Type something for me to say!")

    while True:
        text = input("\n🎤 You: ").strip()
        if text.lower() == 'exit':
            speak(engine, "Goodbye!")
            break

        elif text.lower() == 'sample':
            phrase = random.choice(get_samples())
            print(f"🎲 {phrase}")
            speak(engine, phrase)
        elif text:
            speak(engine, text)
        else:
            print("💡 Type 'sample' for ideas or 'exit to quit'")

if __name__ == "__main__":
    main()

