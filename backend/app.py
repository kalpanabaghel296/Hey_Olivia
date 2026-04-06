from flask import Flask, request, jsonify
from backend.voice.listener import listen_command
from backend.brain.processor import process_command

print("🚀 Starting Olivia Backend...")

app = Flask(__name__)


@app.route("/")
def home():
    return "AI Voice Assistant is running!"


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


if __name__ == "__main__":
    print("🔥 Flask server starting on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)