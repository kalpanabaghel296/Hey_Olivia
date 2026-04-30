import json
import os
import webbrowser
import subprocess

DATA_FILE = os.path.join(os.path.dirname(__file__), "commands.json")

def run_command(keyword):
    keyword = keyword.lower().strip()

    if not os.path.exists(DATA_FILE):
        return False

    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return False
            commands = json.loads(content)
    except:
        return False

    for cmd in commands:
        if cmd["keyword"] == keyword:
            for action in cmd["actions"]:
                try:
                    if action.startswith("http"):
                        webbrowser.open(action)
                    else:
                        subprocess.Popen(action, shell=True)
                except:
                    pass
            return True

    return False