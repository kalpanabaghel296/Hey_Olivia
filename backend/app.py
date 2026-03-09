from flask import Flask,request, jsonify
from backend.voice.listener import listen_command
from backend.brain.processor import process_command

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Voice Assistant is running!"

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    text = data.get("text", "")

    intent, response = process_command(text)

    return jsonify({
        "intent": intent,
        "response": response
    })

@app.route("/listen")
def listen():
    text = listen_command()
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)