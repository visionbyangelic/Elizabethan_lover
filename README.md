# 🎭 The Elizabethan Lover: An AI Bard

> *"Dost thou question the very breath that doth escape my lips?"*

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Tech Stack](https://img.shields.io/badge/Stack-Flask_%7C_Gemini_2.5_%7C_PyTorch-blueviolet)
![License](https://img.shields.io/badge/License-MIT-blue)

**The Elizabethan Lover** is a full-stack Generative AI application that speaks exclusively in Early Modern English (Shakespearean). Unlike generic chatbots, this project enforces a rigid historical persona using System Prompt Engineering and Google's latest **Gemini 2.5 Flash** architecture.

---

## 📖 The "Fail & Fix" Architecture Story

This project is a tale of two halves: **The Research** and **The Product**.

### 🧪 Phase 1: The Research (The "Fail")
*Located in `/research`*

I initially attempted to build a Large Language Model (LLM) from scratch to understand the math behind the magic.
* **The Goal:** Train a Transformer model on the complete works of William Shakespeare (`pg100.txt`).
* **The Fail:**
    1.  **Dirty Data:** The raw dataset contained 20% legal boilerplate (Project Gutenberg licenses), causing the model to generate copyright notices instead of poetry.
    2.  **Goldfish Memory:** My custom Bigram and Transformer models (built with PyTorch) had a limited context window (64 characters) and were computationally expensive to host.
* **The Fix:** I wrote a custom cleaning pipeline to surgically slice the text and validated the Transformer architecture, achieving a Cross-Entropy Loss drop from **2.64** (Bigram) to **1.84** (GPT).

### 🚀 Phase 2: The Product (The "Fix")
*Located in `/backend` and `/frontend`*

To build a viable production app with low latency and long-term memory, I pivoted the architecture.
* **The Brain:** I replaced the custom model with **Google Gemini 2.5 Flash** (November 2025).
* **The Persona:** I engineered a strict System Prompt that forces the LLM to treat modern technology as "sorcery" and maintain iambic cadence.
* **The Bridge:** A Python Flask server connects the vanilla JS frontend to the Google Cloud API.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JS | "Parchment" aesthetic with dynamic DOM manipulation. |
| **Backend** | Python, Flask | REST API acting as the bridge between client and AI. |
| **AI Engine** | Google Gemini 2.5 | `gemini-2.5-flash` model via `google-generativeai` SDK. |
| **Research** | PyTorch, Pandas | Custom Tokenizer and Transformer implementation. |
| **Tools** | VS Code, Git | Version control and development environment. |

---

## 📂 Repository Structure

```text
Elizabethan-Lover/
├── backend/               # THE BRAIN (Production)
│   ├── app.py             # Flask Server & Gemini Integration
│   ├── diagnose.py        # Utility to check available Google Models
│   └── requirements.txt   # Dependencies
│
├── frontend/              # THE FACE (UI)
│   ├── index.html         # The Chat Interface
│   ├── style.css          # Parchment/Leather styling
│   └── script.js          # Fetch logic to talk to Flask
│
├── research/              # THE LAB (Data Science)
│   └── shakespeare_gpt_trainer.ipynb  # The cleaning & training logs
│
└── README.md              # You are here
💻 How to Run This Project Locally
Prerequisites
Python 3.8+

A Google Gemini API Key (Get one here)

1. Clone the Repository
Bash

git clone [https://github.com/YOUR_USERNAME/Elizabethan-Lover.git](https://github.com/YOUR_USERNAME/Elizabethan-Lover.git)
cd Elizabethan-Lover
2. Setup the Backend
Navigate to the backend folder and install dependencies:

Bash

cd backend
pip install -r requirements.txt
Configuration: Open app.py and replace the placeholder with your API Key:

Python

GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
3. Wake the Bard
Run the Flask server:

Bash

python app.py
You should see: Running on http://127.0.0.1:5000

4. Open the Frontend
Navigate to the frontend folder and open index.html in your browser.

📸 Demo
User: "What is the internet?" Elizabethan Lover: "By my troth, I know not of this 'inner-net'. 'Tis sounds like a sorcerer's web designed to ensnare the minds of men! Speak not of such dark magic, lest the spirits hear thee."