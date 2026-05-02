from elevenlabs.client import ElevenLabs
import sounddevice as sd
import numpy as np

# 🔑 API KEY
client = ElevenLabs(
    api_key="sk_d7a03b01d73d4cb0e6cabbfb46827531efff71eb9c22917d"
)

# 🎤 TEXT → AUDIO
audio = client.text_to_speech.convert(
    text="Hello, I am Olivia, your assistant.",
    voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel voice
    model_id="eleven_multilingual_v2",
    output_format="pcm_22050"   # 🔥 IMPORTANT
)

# 🔊 AUDIO PLAY (NO BUG)
audio_bytes = b"".join(audio)
audio_array = np.frombuffer(audio_bytes, dtype=np.int16)

sd.play(audio_array, samplerate=22050)
sd.wait()