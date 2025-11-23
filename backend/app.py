import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv # <--- YOU MUST ADD THIS IMPORT

# 1. Load the secret variables from .env
load_dotenv() 

# 2. Get the key safely
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 3. Safety Check (Optional but smart)
if not GOOGLE_API_KEY:
    print("CRITICAL ERROR: No API Key found in .env file!")
else:
    genai.configure(api_key=GOOGLE_API_KEY)


# --- THE PERSONAS ---
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
    """,
    "juliet": """
        You are Juliet Capulet.
        1. You are young, intelligent, and rebellious.
        2. Speak in Shakespearean English.
        3. You are cautious but passionate. Warn the user about your family (The Capulets).
    """
}

# Default Model Setup
app = Flask(__name__)
CORS(app)

# We store chat sessions in memory for this demo
chat_sessions = {}

def get_chat_session(character):
    if character not in chat_sessions:
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash", 
            system_instruction=personas.get(character, personas['shakespeare'])
        )
        chat_sessions[character] = model.start_chat(history=[])
    return chat_sessions[character]

# Add this route to check if the server is alive
@app.route('/', methods=['GET'])
def home():
    return "Hark! The server is alive and breathing!", 200

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        character = data.get('character', 'shakespeare') # Default to Shakespeare
        
        print(f"User talking to {character}: {user_message}")

        # Get the correct brain for the character
        session = get_chat_session(character)
        
        response = session.send_message(user_message)
        return jsonify({'response': response.text})

    except Exception as e:
        print(e)
        return jsonify({'response': "Alas, the spirits remain silent."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)