import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets.get("GEMINI_API_KEY", None)
    except Exception:
        api_key = None

if not api_key:
    raise ValueError("Gemini API key was not found.")

client = genai.Client(api_key=api_key)

def get_chat_response(chat_session, prompt):
    try:
        response = chat_session.send_message_stream(prompt)
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            yield "Quota limit reached. Please wait one minute and try again."
        else:
            yield f"API Error: {error_msg}"