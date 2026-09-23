import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Local testing ke liye .env load karein
load_dotenv()

# Pehle Streamlit secrets check karein, agar na mile toh os.getenv (local .env)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def get_ai_response(messages_history):
    """Active Groq model se response generate karta hai."""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages_history,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"