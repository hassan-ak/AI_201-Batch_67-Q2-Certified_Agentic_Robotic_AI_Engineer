import requests
import json
from openrouter.secrets import secrets
from rich import print


def openrouter_gemini():
    response = requests.post(
        url=f"{secrets['OPENROUTER_API_URL']}/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['OPENROUTER_API_KEY']}",
        },
        data=json.dumps(
            {
                "model": secrets['OPENROUTER_GEMINI_MODEL'],
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
        url=f"{secrets['OPENROUTER_API_URL']}/chat/completions",
        headers={
            "Authorization": f"Bearer {secrets['OPENROUTER_API_KEY']}",
        },
        data=json.dumps(
            {
                "model": secrets["OPENROUTER_DEEPSEEK_MODEL"],
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
    
