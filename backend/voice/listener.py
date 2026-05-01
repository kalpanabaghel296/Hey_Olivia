import speech_recognition as sr
import time


recognizer = sr.Recognizer()

# ---------------- MICROPHONE OPTIMIZATION ----------------
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def listen_command(timeout=3, phrase_time_limit=5):

    with sr.Microphone(sample_rate=16000) as source:

        print("🎧 Calibrating background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎤 Listening for command...")

        try:
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        except sr.WaitTimeoutError:
            return ""

    # ---------------- SPEECH RECOGNITION ----------------

    try:

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()

        print("🧠 Recognized:", command)

        return command

    except sr.UnknownValueError:
        print("⚠ Could not understand audio")
        return ""

    except sr.RequestError:
        print("⚠ Speech recognition service unavailable")
        return ""


# ---------------- WAKE WORD LISTENER ----------------

def listen_wake_word(wake_words=("olivia", "hey olivia")):

    with sr.Microphone(sample_rate=16000) as source:

        print("🟢 Waiting for wake word:", wake_words)

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=3
            )

        except sr.WaitTimeoutError:
            return False

    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()

        print("Heard:", text)

        if any(word in text for word in wake_words):

            if len(text.split()) <= 3:
                print("🔔 Wake word detected")
                return True

        return False

    except:
        return False