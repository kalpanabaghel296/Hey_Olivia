import subprocess
import os
import uuid
import winsound

# 🔥 BASE PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

PIPER_DIR = os.path.join(BASE_DIR, "backend", "voice_model")

PIPER_PATH = os.path.join(PIPER_DIR, "piper.exe")
MODEL_PATH = os.path.join(PIPER_DIR, "en_US-lessac-medium.onnx")


def speak(text):
    try:
        # ❌ skip useless text
        if not text or text.lower() == "could not understand":
            print("⚠️ Skipping TTS")
            return

        filename = os.path.join(BASE_DIR, f"temp_{uuid.uuid4().hex}.wav")

        process = subprocess.Popen(
            [PIPER_PATH, "-m", MODEL_PATH, "-f", filename],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=PIPER_DIR
        )

        out, err = process.communicate(input=text)

        if err:
            print("PIPER LOG:", err)

        if not os.path.exists(filename):
            print("❌ WAV file not created")
            return

        # 🔊 PLAY AUDIO (NO POPUP, NO LIB INSTALL)
        winsound.PlaySound(filename, winsound.SND_FILENAME)

        os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)