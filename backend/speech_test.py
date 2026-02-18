import sounddevice as sd
import numpy as np
import speech_recognition as sr

fs = 16000        # Sample rate
seconds = 5

print("🎤 Speak now...")

# Record audio (float32)
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

# Convert float32 → int16 PCM
audio_int16 = np.int16(audio * 32767)

# Create AudioData object directly (NO WAV FILE)
audio_data = sr.AudioData(
    audio_int16.tobytes(),
    sample_rate=fs,
    sample_width=2   # 16-bit = 2 bytes
)

r = sr.Recognizer()

try:
    text = r.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Speech service error:", e)
