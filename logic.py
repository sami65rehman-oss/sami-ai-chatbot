import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq Client
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def get_ai_response(messages_history):
    """Active Groq model se response generate karta hai."""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",  # Official active model according to Groq docs
            messages=messages_history,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"