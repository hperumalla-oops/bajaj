import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=AIzaSyAHHXYaCKoa67OQc5_6eOtGnkeuZUcudjU)
model = genai.GenerativeModel("gemini-pro")

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
