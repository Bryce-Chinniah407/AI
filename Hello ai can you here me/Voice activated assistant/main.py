import pyttsx3
import speech_recognition as sr
from datetime import datetime

VOICE_INDEX = 1
SPEECH_RATE = 150
user_name = ""

def speak(text):
    print("🤖 Assistant: ", text)
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[VOICE_INDEX].id)
    engine.setProperty("rate", SPEECH_RATE)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone()as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"✅ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, didn't catch that.")
    except sr.RequestError:
        speak("There was a network issue.")

    return ""

def respond_to_command(command):
    global user_name, VOICE_INDEX

    if "hello" in command:
        speak(f"Hi {user_name}!" if user_name else "Hello! How can I help you?")
    
    elif "your name" in command:
        speak("I am your smart Python assistant.")

    elif "time" in command:
        speak(f"The time is {datetime.now().strftime('%H:%M')}")

    elif "date" in command:
        speak(f"Taday is {datetime.now().strftime('%B %d, %Y')}")

    elif "my name is" in command:
        user_name = command.replace("my name is", "").strip().captalize()
        speak(f"Nice to meet you, {user_name}")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    
    else:
        speak("I'm not sure i can help with that.")

    return True

def main():
    speak("Voice assistant activated. Say something")
    while True:
         command = get_audio()
         if command and not respond_to_command(command):
             break
         
if __name__ == "__main__":
    main()