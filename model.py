import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# api_key = 'AIzaSyAHHXYaCKoa67OQc5_6eOtGnkeuZUcudjU'

# genai(api_key=api_key)
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(context, question):
    prompt = f"""
You are answering a question based on a document.

Context:
{context}

Question:
{question}

Only answer from the context.
"""
    response = model.generate_content(prompt)
    return response.text
