import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq Client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_ai_response(messages_history):
    """Groq API ko call karta hai aur fast response return karta hai."""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",  # Currently active production model
            messages=messages_history,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"