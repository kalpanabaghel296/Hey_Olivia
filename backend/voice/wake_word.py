import sounddevice as sd
import numpy as np
import speech_recognition as sr

WAKE_WORD = "olivia"

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
        return WAKE_WORD in text
    except:
        return False
