import sounddevice as sd
import numpy as np
import speech_recognition as sr
import threading
import os
from playsound import playsound

WAKE_WORD = "olivia"


def play_listening_sound():
    def _play():
        sound_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "assets",
            "listening.mp3"
        )
        playsound(sound_path)

    threading.Thread(target=_play, daemon=True).start()


def listen_for_wake_word():
    fs = 16000
    r = sr.Recognizer()

    print("🟢 Waiting for wake word: 'olivia'")

    audio = sd.rec(int(3 * fs), samplerate=fs, channels=1)
    sd.wait()

    audio_int16 = np.int16(audio * 32767)
    audio_data = sr.AudioData(
        audio_int16.tobytes(),
        sample_rate=fs,
        sample_width=2
    )

    try:
        text = r.recognize_google(audio_data).lower()
        print("Heard:", text)

        if WAKE_WORD in text:
            print("🔔 Wake word detected")

            play_listening_sound()  # 🔥 sound plays here

            return True

        return False

    except Exception as e:
        print("Error:", e)
        return False
    
    