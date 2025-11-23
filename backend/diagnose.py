import os
import google.generativeai as genai
from dotenv import load_dotenv # Import the loader

# 1. Load the hidden key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

print("--- AVAILABLE MODELS ---")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Name: {m.name}")