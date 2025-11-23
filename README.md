

# 🎭 The Elizabethan Lover: An AI Bard

> *"Dost thou question the very breath that doth escape my lips?"*

[![Live Demo](https://img.shields.io/badge/Live_Demo-Visit_App-success?style=for-the-badge&logo=vercel)](https://elizabethan-lover.vercel.app)
![Tech Stack](https://img.shields.io/badge/Stack-Flask_%7C_Gemini_2.5_%7C_Vercel-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

**The Elizabethan Lover** is a full-stack Generative AI application that simulates a "Snapchat" experience with historical figures. Unlike generic chatbots, this project enforces rigid historical personas (Shakespeare, Romeo, Juliet) using System Prompt Engineering and Google's **Gemini 2.5 Flash** architecture.

---
````markdown
## 📖 The "Fail & Fix" Architecture Story

This project is a tale of two halves: **The Data Science** (Research) and **The Product Engineering** (Web).

### 🧪 Phase 1: The Research (The "Fail")
*Located in `/research`*

I initially attempted to build a Large Language Model (LLM) from scratch to understand the math behind the magic.
* **The Goal:** Train a Transformer model on the complete works of William Shakespeare (`pg100.txt`).
* **The Fail:**
    1.  **Dirty Data:** The raw dataset contained 20% legal boilerplate, causing the model to generate copyright notices instead of poetry.
    2.  **Goldfish Memory:** My custom Transformer model (built with PyTorch) had a limited context window (64 characters) and was computationally expensive to host.
* **The Fix:** I wrote a custom cleaning pipeline to surgically slice the text and validated the Self-Attention architecture, achieving a Cross-Entropy Loss drop from **2.64** (Bigram) to **1.84** (GPT).

### 🚀 Phase 2: The Product (The "Fix")
*Located in `/web`*

To build a viable production app with low latency, I pivoted the architecture.
* **The Brain:** I replaced the custom model with **Google Gemini 2.5 Flash**.
* **The Pivot:** Instead of training a model, I used **System Prompt Engineering** to create distinct personas for Shakespeare, Romeo, and Juliet.
* **The Challenge:** The AI initially refused to be romantic (Google Safety Filters). I had to programmatically disable specific harassment/sexual filters to allow Romeo to be "impulsive and dramatic" without crashing the app.
* **The UI:** A mobile-first "Snapchat Clone" built with Vanilla JS and CSS Flexbox to handle dynamic viewport heights (`100dvh`) on mobile devices.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JS | "Snapchat" Dark Mode aesthetic. Mobile-responsive. |
| **Backend** | Python, Flask | Serverless API deployed on Vercel. |
| **AI Engine** | Google Gemini 2.5 | `gemini-2.5-flash` with disabled safety filters. |
| **Research** | PyTorch, Pandas | Custom Tokenizer and Transformer implementation. |
| **Deployment** | Vercel | Monorepo structure with serverless function routing. |

---

## 📂 Repository Structure

```text
Elizabethan-Lover/
├── research/              # THE LAB (Data Science)
│   └── shakespeare_gpt_trainer.ipynb  # The cleaning & training logs
│
├── web/                   # THE APP (Production Vercel Build)
│   ├── api/               # THE KITCHEN (Backend)
│   │   └── chat.py        # Flask Serverless Function
│   │
│   ├── public/            # THE BUFFET (Frontend)
│   │   ├── index.html     # The UI
│   │   ├── style.css      # Mobile-first CSS
│   │   ├── script.js      # Fetch logic & Persona switching
│   │   └── images/        # Local assets (PFPs)
│   │
│   └── requirements.txt   # Dependencies
│
└── README.md              # You are here
````

-----

## 💻 How to Run This Project Locally

### Prerequisites

  * Python 3.8+
  * A Google Gemini API Key

### 1\. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/Elizabethan-Lover.git](https://github.com/YOUR_USERNAME/Elizabethan-Lover.git)
cd Elizabethan-Lover
```

### 2\. Setup the Environment

Navigate to the web folder and install dependencies:

```bash
cd web
pip install -r requirements.txt
```

### 3\. Configure Secrets

Create a `.env` file inside the `web` folder:

```text
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4\. Wake the Bard

Run the Flask server:

```bash
python api/chat.py
```

*You should see: `Running on http://127.0.0.1:5000`*

### 5\. Open the Frontend

Open `web/public/index.html` in your browser.

-----

## 📸 Personas

  * **William Shakespeare:** Wise, poetic, treats technology as sorcery.
  * **Romeo Montague:** Impulsive, dramatic, constantly references the moon.
  * **Juliet Capulet:** Cautious but passionate, warns you about her family.

-----

## 🤝 License

MIT License. Created by Angelic C.

```
```
