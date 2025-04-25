import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENROUTER_API_KEY environment variable."
    )
BASE_URL = os.getenv("OPENROUTER_API_URL")
if not BASE_URL:
    raise ValueError(
        "Base URL not found. Please set the OPENROUTER_API_URL environment variable."
    )
gemini_model = os.getenv("OPENROUTER_GEMINI_MODEL")
if not gemini_model:
    raise ValueError(
        "Gemini model not found. Please set the OPENROUTER_GEMINI_MODEL environment variable."
    )
deepseek_model = os.getenv("OPENROUTER_DEEPSEEK_MODEL")
if not deepseek_model:
    raise ValueError(
        "Deepseek model not found. Please set the OPENROUTER_DEEPSEEK_MODEL environment variable."
    )


def openrouter_gemini():
    response = requests.post(
        url=f"{BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        data=json.dumps(
            {
                "model": gemini_model,
                "messages": [
                    {
                        "role": "user",
                        "content": "What is the meaning of life, respond in a couples lines?",
                    }
                ],
            }
        ),
    )
    data = response.json()
    print('\n')
    print(data['choices'][0]['message']['content'])
    print('\n')
    
    
def openrouter_deepseek():
    response = requests.post(
        url=f"{BASE_URL}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        data=json.dumps(
            {
                "model": deepseek_model,
                "messages": [
                    {
                        "role": "user",
                        "content": "Is time the fourth dimension, respond in a couples lines?",
                    }
                ],
            }
        ),
    )
    data = response.json()
    print('\n')
    print(data['choices'][0]['message']['content'])
    print('\n')
    
