import sounddevice as sd
import numpy as np
import speech_recognition as sr

def listen_command(seconds=5):
    fs = 16000
    r = sr.Recognizer()

    print("🎤 Listening for command (5 sec)...")

    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    audio_int16 = np.int16(audio * 32767)
    audio_data = sr.AudioData(
        audio_int16.tobytes(),
        sample_rate=fs,
        sample_width=2
    )

    try:
        return r.recognize_google(audio_data)
    except:
        return "Could not understand"
