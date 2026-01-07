import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

recognizer = sr.Recognizer()
translator = Translator()

def sepeech_to_text():
    with sr.Microphone() as source:
        print("🎤 Speak in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("📄 You said:", text)
        return text
    except:
        print("❌ Could not understand speech")
        return None
    
def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    print("🌏 translated: ", translated.text)
    return translated.text

def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def select_language():
    print("\n🌍 Choose language: ")
    print("1/. French")
    print("2/. Spanish")
    print("3/. Hindi")
    print("4/. German")
    print("5/. Russian")
    print("6/. Japanese")

    return {
        "1": "fr",
        "2": "es",
        "3": "hi",
        "4": "de",
        "5": "ru",
        "6": "ja"
    }.get(input("Enter Choice: "), "hi")

def main():
    lang = select_language()
    text = sepeech_to_text()
    
    if text:
        translated = translate_text(text, lang)
        print("🔊 Speaking... ")
        speak(translated, lang)
        print("✅ Done !")

if __name__ == "__main__":
    main()