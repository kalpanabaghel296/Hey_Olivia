import requests
from backend.voice.wake_word import listen_for_wake_word
from backend.commands.command_listener import listen_command
from backend.utils.translator import to_english
from backend.voice.tts import speak


FLASK_URL = "http://localhost:5000/process"

print("🤖 Olivia Assistant started")

while True:
    woke = listen_for_wake_word()

    if woke:
        print("🔔 Wake word detected")

        command = listen_command(seconds=4)
        print("🧠 Raw command:", command)

        english_command = to_english(command)
        print("🌐 Translated:", english_command)

        response = requests.post(
            FLASK_URL,
            json={"text": english_command}
        ).json()

        reply = response["response"]
        print("🤖 Reply:", reply)

        speak(reply)

        print("😴 Sleeping...\n")