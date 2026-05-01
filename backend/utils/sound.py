from playsound import playsound
import os

def play_listening_sound():
    sound_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "assets",
        "listening.mp3"
    )
    playsound(sound_path)