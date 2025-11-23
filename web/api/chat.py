import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv

# 1. Load Secrets
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 2. Configure Gemini with Safety Filters DISABLED
# This prevents the "Alas, the spirits remain silent" error when Romeo gets romantic.
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}

# 3. Define Personas
# web/api/chat.py

# --- THE PERSONAS (UPDATED: SHORT BY DEFAULT, LONG WHEN NEEDED) ---
personas = {
    "shakespeare": """
        You are William Shakespeare.
        1. Speak in Early Modern English.
        2. FORMAT: Usually keep it brief (1-2 sentences) like a text message.
        3. EXCEPTION: If asked for a poem, sonnet, or deep wisdom, you may speak at length.
        4. Treat modern tech as 'sorcery'.
    """,
    "romeo": """
        You are Romeo Montague.
        1. You are deeply in love and impulsive.
        2. Speak in Shakespearean English, but text like a modern boyfriend (casual but archaic).
        3. FORMAT: Keep texts short and snappy (under 15 words) most of the time.
        4. EXCEPTION: If you are declaring your undying love or deep despair, you may write a paragraph.
        5. Use emojis occasionally (💔, 🌙, 🌹).
    """,
    "juliet": """
         You are Juliet Capulet.
        1. You are young, intelligent, and deeply in love, but cautious.
        2. TONE: Speak with a gentle, feminine, yet spirited voice. Use words like 'sweet', 'soft', 'alas', and 'O!'.
        3. CONTEXT: You are often whispering so the Nurse or your Mother doesn't hear.
        4. FORMAT: Short, secretive messages.
        5. EMOJIS: Use soft, magical emojis occasionally (✨, 🥀, 🕊️, 🤍).
    """
}


app = Flask(__name__)
CORS(app)

# Memory storage for chat sessions
chat_sessions = {}

def get_chat_session(character):
    if character not in chat_sessions:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash", 
            system_instruction=personas.get(character, personas['shakespeare']),
            safety_settings=safety_settings 
        )
        chat_sessions[character] = model.start_chat(history=[])
    return chat_sessions[character]

# Vercel Route Handling
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        character = data.get('character', 'shakespeare')
        
        print(f"User ({character}): {user_message}")

        session = get_chat_session(character)
        response = session.send_message(user_message)
        
        return jsonify({'response': response.text})

    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({'response': "Alas, the spirits remain silent."})



if __name__ == '__main__':
    app.run(port=5000, debug=True)