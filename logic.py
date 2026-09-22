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
    raise ValueError("⚠️ Gemini API key is not found!")

client = genai.Client(api_key=api_key)

def get_gemini_response(prompt):
    try:
        # Strictly using gemini-2.5-flash to bypass 3.6 rate limits
        response = client.models.generate_content_stream(
            model="gemini-2.5-flash",
            contents=prompt
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"⚠️ API Error: {str(e)}"