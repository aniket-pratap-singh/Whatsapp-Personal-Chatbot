from openai import OpenAI
from google_services import get_classroom_service, get_gmail_service
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

api_key = os.getenv("OPENROUTER_API_KEY")

def get_response(entry):
    
    last_message = entry["content"]
    if (last_message.lower()=="gmail"):
        return get_gmail_service()
    elif (last_message.lower()=="classroom"):
        return get_classroom_service()


    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": last_message}
    ]

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    
    response = client.chat.completions.create(
            model="tngtech/deepseek-r1t2-chimera:free",
            messages=messages,
            temperature=0.7)
        



    reply = response.choices[0].message.content
    addon= '🤖:  \n'
    reply = addon + reply.strip()
    return reply


