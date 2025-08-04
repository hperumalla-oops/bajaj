import google.generativeai as genai
import openai as OpenAI
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
        - Try to explain briefly but mention all important information
        - Try to keep it below 50 words 
        - if asked about about numeric information, for example, number of days, monetary charges etc, mention the amount in numbers
       
Context:
{context}

Question:
{question}

Only answer from the context.
"""
    response = model.generate_content(prompt)
    return response.text


