import requests
from backend.voice.wake_word import listen_for_wake_word
from backend.commands.command_listener import listen_command
from backend.utils.translator import to_english
from backend.voice.tts import speak

FLASK_URL = "http://localhost:5000/process"

print("🤖 Olivia Assistant started")


def send_request(text):
    try:
        response = requests.post(
            FLASK_URL,
            json={"text": text},
            timeout=5
        )

        return response.json()

    except requests.exceptions.ConnectionError:
        return {"response": "Backend server is not running"}

    except Exception as e:
        return {"response": f"Request error: {str(e)}"}


while True:
    try:
        woke = listen_for_wake_word()

        if not woke:
            continue

        print("🔔 Wake word detected")

        command = listen_command(seconds=4)

        if not command:
            print("⚠️ No command detected")
            speak("I did not hear anything")
            continue

        print("🧠 Raw command:", command)

        # optional translation (safe)
        english_command = to_english(command)
        print("🌐 Translated:", english_command)

        result = send_request(english_command)

        reply = result.get("response", "No response received")

        print("🤖 Reply:", reply)

        speak(reply)

        print("😴 Sleeping...\n")

    except KeyboardInterrupt:
        print("\n🛑 Assistant stopped")
        break

    except Exception as e:
        print("❌ Assistant error:", e)
        speak("Something went wrong")