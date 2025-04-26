from litellm_basic.secerts import gemini_api_key, gemini_model, groq_api_key, groq_model
from litellm import completion


messages = [{"role": "user", "content": "What is AI?"}]


def run_gemini():
    print("\nRunning Gemini...\n")
    result = completion(
        api_key=gemini_api_key,
        model=gemini_model,
        messages=messages,
    )
    print(result["choices"][0]["message"]["content"])
    
    

def run_groq():
    print("\nRunning Groq...\n")
    result = completion(
        api_key=groq_api_key,
        model=groq_model,
        messages=messages,
        stream=True,
    )
    for chunk in result:
        print(chunk["choices"][0]["delta"]["content"], end="")
