import os
from dotenv import load_dotenv

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

gemini_model = os.getenv("GEMINI_MODEL")
if gemini_model is None:
    raise ValueError("GEMINI_MODEL is not set in the environment variables.")

groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

groq_model = os.getenv("GROQ_MODEL")
if groq_model is None:
    raise ValueError("GROQ_MODEL is not set in the environment variables.")