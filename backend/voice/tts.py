import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 190)

def speak(text):
    print(f"Olivia: {text}")
    engine.say(text)
    engine.runAndWait()