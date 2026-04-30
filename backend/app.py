from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

from backend.voice.listener import listen_command
from backend.brain.processor import process_command
from backend.run_command import run_command

print("🚀 Starting Olivia Backend...")

app = Flask(__name__)
CORS(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), "commands.json")


# ---------------- FILE HELPERS ----------------
def load_commands():
    try:
        if not os.path.exists(DATA_FILE):
            return []

        if os.path.getsize(DATA_FILE) == 0:
            return []

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except Exception as e:
        print("❌ Load error:", e)
        return []


def save_commands(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("❌ Save error:", e)


# ---------------- BASIC ROUTES ----------------
@app.route("/")
def home():
    return "AI Voice Assistant is running!"


# ---------------- COMMAND CRUD ----------------

# ADD / UPDATE
@app.route("/command", methods=["POST"])
def add_command():
    try:
        data = request.get_json()

        keyword = data.get("keyword", "").lower().strip()
        actions = data.get("actions", [])

        if not keyword:
            return jsonify({"error": "keyword required"}), 400

        if not isinstance(actions, list) or not (1 <= len(actions) <= 5):
            return jsonify({"error": "1-5 actions required"}), 400

        commands = load_commands()

        # overwrite existing
        commands = [c for c in commands if c.get("keyword") != keyword]

        commands.append({
            "keyword": keyword,
            "actions": actions
        })

        save_commands(commands)

        return jsonify({"message": "saved"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# GET ALL
@app.route("/commands", methods=["GET"])
def get_commands():
    return jsonify(load_commands())


# DELETE
@app.route("/command/<keyword>", methods=["DELETE"])
def delete_command(keyword):
    try:
        keyword = keyword.lower().strip()

        commands = load_commands()
        commands = [c for c in commands if c.get("keyword") != keyword]

        save_commands(commands)

        return jsonify({"message": "deleted"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- EXECUTE ----------------
@app.route("/execute", methods=["POST"])
def execute():
    try:
        keyword = request.json.get("keyword", "").lower().strip()

        if run_command(keyword):
            return jsonify({"message": "executed"})
        else:
            return jsonify({"error": "not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------- NLP PROCESS ----------------
@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "intent": "ERROR",
                "response": "No JSON data received"
            }), 400

        text = data.get("text", "").strip()

        if not text:
            return jsonify({
                "intent": "ERROR",
                "response": "No input text provided"
            }), 400

        intent, response = process_command(text)

        return jsonify({
            "intent": intent,
            "response": response
        })

    except Exception as e:
        print("❌ Error in /process:", e)

        return jsonify({
            "intent": "ERROR",
            "response": f"Internal server error: {str(e)}"
        }), 500


# ---------------- VOICE ----------------
@app.route("/listen")
def listen():
    try:
        text = listen_command()

        return jsonify({
            "text": text
        })

    except Exception as e:
        print("❌ Error in /listen:", e)

        return jsonify({
            "text": "",
            "error": str(e)
        }), 500


# ---------------- START SERVER ----------------
if __name__ == "__main__":
    print("🔥 Flask server starting on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)