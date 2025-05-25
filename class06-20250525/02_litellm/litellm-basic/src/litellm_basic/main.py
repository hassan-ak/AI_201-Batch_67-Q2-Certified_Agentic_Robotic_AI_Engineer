from litellm_basic.secerts import gemini_api_key, gemini_model, groq_api_key, groq_model
from litellm import completion
from rich import print
from litellm_basic.secerts import Secrets


messages = [{"role": "user", "content": "What is AI?"}]

secrets = Secrets()

def run_gemini():
    print("\nRunning Gemini...\n")
    result = completion(
        api_key=secrets.gemini_api_key,
        model=secrets.gemini_model,
        messages=messages,
    )
    print(result["choices"][0]["message"]["content"])
    
    
def run_groq():
    print("\nRunning Groq...\n")
    result = completion(
        api_key=secrets.groq_api_key,
        model=secrets.groq_model,
        messages=messages,
        stream=True,
    )
    for chunk in result:
        print(chunk["choices"][0]["delta"]["content"], end="")