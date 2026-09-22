import os
from dotenv import load_dotenv
from google import genai
load_dotenv(dotenv_path=".env")
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None
def get_ai_response(user_prompt):
    if not api_key:
        yield "⚠️ Error: Gemini API key is not found in enviroment variables."
        return
    try:
        response = client.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=user_prompt
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"⚠️ Connection Error: {str(e)}"