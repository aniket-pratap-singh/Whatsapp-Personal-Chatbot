from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
from openrouter_responder import get_response
from groq_responder import get_response as groq_get_response

app = Flask(__name__)
LOG_FILE = 'chat_history.json'


@app.route('/store_message', methods=['POST'])
def store_message():
    data = request.get_json()
    message = data.get('message', '')
    
    if not message:
        return jsonify({"status": "error", "message": "Empty message"}), 400

    # Load existing history
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            history = json.load(f)
    else:
        history = []

    entry = {
        "content": message,
        "timestamp": datetime.now().isoformat()
    }
    history.append(entry)

    # Save back to JSON
    with open(LOG_FILE, 'w') as f:
        json.dump(history, f, indent=2)

    reply = groq_get_response(entry)
    return jsonify({"status": "success", "reply": reply})

if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=True)



