import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_url = os.getenv("OPENROUTER_API_URL")
openrouter_gemini_model = os.getenv("OPENROUTER_GEMINI_MODEL")
openrouter_deepseek_model = os.getenv("OPENROUTER_DEEPSEEK_MODEL")


if not openrouter_api_key or not openrouter_api_url or not openrouter_gemini_model or not openrouter_deepseek_model:
    print("[red]Please set the OPENROUTER_API_KEY, OPENROUTER_API_URL, OPENROUTER_GEMINI_MODEL, and OPENROUTER_DEEPSEEK_MODEL environment variables.[/red]")
    exit(1)

secrets = {
    "OPENROUTER_API_KEY": openrouter_api_key,
    "OPENROUTER_API_URL": openrouter_api_url,
    "OPENROUTER_GEMINI_MODEL": openrouter_gemini_model,
    "OPENROUTER_DEEPSEEK_MODEL": openrouter_deepseek_model,
}