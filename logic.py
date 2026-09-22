import os
from google import genai

# 1. Pehle local environment variable (.env) se key check karein
api_key = os.getenv("GEMINI_API_KEY")

# 2. Agar .env mein na mile, toh Streamlit Cloud Secrets se check karein
if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets.get("GEMINI_API_KEY", None)
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("⚠️ Gemini API key is not found! Check your .env file locally or Secrets on Streamlit Cloud.")

# Gemini Client initialize karein
client = genai.Client(api_key=api_key)

def get_gemini_response(prompt):
    try:
        # Rate limit se bachne ke liye gemini-2.5-flash use kar rahe hain
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=prompt
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"⚠️ API Error: {str(e)}"