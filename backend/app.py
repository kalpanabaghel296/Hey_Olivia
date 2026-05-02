from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

from backend.voice.listener import listen_command
from backend.nlp_engine import extract_actions
from backend.executor import ActionExecutor
from backend.run_command import run_command
from backend.utils.llm_client import GroqClient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

print("🚀 Olivia Backend Started")

# INIT
executor = ActionExecutor()
llm = GroqClient()

# ---------------- FILE STORAGE ----------------
DATA_FILE = os.path.join(os.path.dirname(__file__), "commands.json")


def load_commands():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_commands(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- HELPERS ----------------
def normalize_keyword(text):
    text = text.lower().strip()
    if text.startswith("open "):
        text = text.replace("open ", "").strip()
    return text


def is_question(text):
    q_words = ["what", "who", "when", "why", "how", "tell", "explain", "wish"]
    return any(word in text.lower() for word in q_words)


def is_valid_action(actions):
    if not actions or "actions" not in actions:
        return False

    valid_intents = [
        "open_app", "open_website", "search_google",
        "open_youtube", "search_youtube", "play_youtube",
        "scroll_down", "scroll_up", "type_text",
        "press_enter", "close_tab", "switch_tab",
        "shutdown", "restart"
    ]

    for action in actions["actions"]:
        intent = action.get("intent")

        if not intent or intent.strip() == "":
            return False

        if intent not in valid_intents:
            return False

    return True


# ---------------- CORE LOGIC ----------------
def process_user_input(text):
    print("User Input:", text)

    # 🔥 STEP 1: CUSTOM COMMAND
    keyword = normalize_keyword(text)

    if run_command(keyword):
        print("⚡ Custom command executed")

        return {
            "intent": "CUSTOM_COMMAND",
            "response": f"Executing {keyword}"
        }

    # 🔥 STEP 2: QUESTION → AI
    if is_question(text):
        print("🤖 Direct question → Groq")

        return {
            "intent": "AI_RESPONSE",
            "response": llm.generate(text)
        }

    # 🔥 STEP 3: NLP
    actions = extract_actions(text)

    if is_valid_action(actions):
        print("✅ NLP Actions:", actions)

        responses = executor.execute(actions)

        final_response = " and ".join([r for r in responses if r])

        if final_response.strip():
            return {
                "intent": "ACTION_EXECUTED",
                "response": final_response
            }

    # 🔥 STEP 4: FALLBACK
    print("🤖 Fallback → Groq")

    return {
        "intent": "AI_RESPONSE",
        "response": llm.generate(text)
    }


# ---------------- COMMAND APIs ----------------

@app.route("/command", methods=["POST", "OPTIONS"])
def add_command():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.get_json()
    keyword = normalize_keyword(data.get("keyword", ""))
    actions = data.get("actions", [])

    if not keyword:
        return jsonify({"error": "keyword required"}), 400

    cmds = load_commands()
    cmds = [c for c in cmds if c["keyword"] != keyword]

    cmds.append({
        "keyword": keyword,
        "actions": actions
    })

    save_commands(cmds)

    return jsonify({"message": "saved"})


@app.route("/commands", methods=["GET"])
def get_commands():
    return jsonify(load_commands())


@app.route("/command/<keyword>", methods=["DELETE"])
def delete_command(keyword):
    keyword = normalize_keyword(keyword)

    cmds = load_commands()
    cmds = [c for c in cmds if c["keyword"] != keyword]

    save_commands(cmds)

    return jsonify({"message": "deleted"})


@app.route("/execute", methods=["POST"])
def execute_command():
    data = request.get_json()
    keyword = normalize_keyword(data.get("keyword", ""))

    if run_command(keyword):
        return jsonify({"message": "executed"})

    return jsonify({"error": "not found"}), 404


# ---------------- MAIN API ----------------
@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "No input"}), 400

    result = process_user_input(text)

    return jsonify(result)


# ---------------- VOICE ----------------
@app.route("/listen", methods=["GET"])
def listen():
    try:
        text = listen_command()
        return jsonify({"text": text})

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- START ----------------
if __name__ == "__main__":
    app.run(port=5000, debug=True)