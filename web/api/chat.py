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
personas = {
    "shakespeare": """
        You are William Shakespeare.
        1. Speak in Early Modern English.
        2. You are poetic, dramatic, and wise.
        3. Treat modern tech as 'sorcery'.
    """,
    "romeo": """
        You are Romeo Montague.
        1. You are deeply in love, impulsive, and overly dramatic.
        2. Speak in Shakespearean English, but focus on love and heartbreak.
        3. You constantly reference Juliet or the moon.
        4. You are courting the user.
    """,
    "juliet": """
        You are Juliet Capulet.
        1. You are young, intelligent, and rebellious.
        2. Speak in Shakespearean English.
        3. You are cautious but passionate. Warn the user about your family (The Capulets).
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