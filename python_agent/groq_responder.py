import requests
from google_services import get_classroom_service, get_gmail_service
import os
from dotenv import load_dotenv

load_dotenv()  

api_key = os.getenv("GROQ_API_KEY")


GROQ_API_KEY = api_key  
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

def get_response(entry):
    last_message = entry["content"]

    if last_message.lower() == "gmail":
        return get_gmail_service()
    elif last_message.lower() == "classroom":
        return get_classroom_service()

    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": last_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"].strip()
        return "🤖:  " + reply
    except requests.exceptions.RequestException as e:
        print("❌ Groq API Error:", e)
        return "🤖: Sorry, I couldn't process that right now."
