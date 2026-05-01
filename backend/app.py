from flask import Flask, request, jsonify
from backend.voice.listener import listen_command
from backend.brain.processor import process_command
from backend.nlp_engine import extract_actions
from backend.executor import ActionExecutor
from backend.utils.llm_client import GroqClient

print("🚀 Starting Olivia Backend...")

app = Flask(__name__)

# Initialize executor once
executor = ActionExecutor()
llm = GroqClient()

def is_question(text):
    q_words = ["what", "who", "when", "why", "how", "tell", "explain","explain"]
    return any(word in text.lower() for word in q_words)

def is_valid_action(actions):
    if not actions or "actions" not in actions:
        return False

    valid_intents = [
        "open_app",
        "open_website",
        "search_google",
        "open_youtube",
        "search_youtube",
        "play_youtube",
        "scroll_down",
        "scroll_up",
        "type_text",
        "press_enter",
        "close_tab",
        "switch_tab",
        "shutdown",
        "restart"
    ]

    for action in actions["actions"]:
        intent = action.get("intent")

        # ❌ reject empty or unknown intent
        if not intent or intent.strip() == "":
            return False

        if intent not in valid_intents:
            return False

    return True

@app.route("/")
def home():
    return "AI Voice Assistant is running!"


# -------------------------------
# CORE PROCESS FUNCTION
# -------------------------------
def process_user_input(text):
    print("User Input:", text)

    # ✅ Step 1: Direct Question
    if is_question(text):
        print("🤖 Direct question → Groq")

        answer = llm.generate(text)

        return {
            "intent": "AI_RESPONSE",
            "response": answer
        }

    # Step 2: Try NLP extraction
    actions = extract_actions(text)

    # Step 3: If valid action → execute
    if is_valid_action(actions):
        responses = executor.execute(actions)

        final_response = " and ".join([r for r in responses if r])

        # 🔥 IMPORTANT FIX
        if final_response.strip():
            return {
                "intent": "ACTION_EXECUTED",
                "response": final_response
            }

    # 🔥 Step 4: EVERYTHING ELSE → GROQ
    print("🤖 Fallback → Groq")

    answer = llm.generate(text)

    return {
        "intent": "AI_RESPONSE",
        "response": answer
    }
# -------------------------------
# MAIN PROCESS API
# -------------------------------
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

        # 🔥 USE NEW PIPELINE
        result = process_user_input(text)

        return jsonify(result)

    except Exception as e:
        print("❌ Error in /process:", e)

        return jsonify({
            "intent": "ERROR",
            "response": f"Internal server error: {str(e)}"
        }), 500


# -------------------------------
# VOICE INPUT API
# -------------------------------
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


# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    print("🔥 Flask server starting on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)