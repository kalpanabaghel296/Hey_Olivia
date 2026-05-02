from backend.brain.processor import process_command
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "commands.json")


def load_commands():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def run_command(keyword):
    commands = load_commands()

    for cmd in commands:
        if cmd.get("keyword") == keyword:

            actions = cmd.get("actions", [])

            for action in actions:
                print(f"🚀 Executing: {action}")

                # 🔥 USE PROCESSOR (BEST)
                process_command(f"open {action}")

            return True

    return False