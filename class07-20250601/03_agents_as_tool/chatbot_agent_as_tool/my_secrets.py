import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print(
        "[red]Error:[/red] [green]GEMINI_API_KEY[/green] is not set in the environment variables."
    )
    exit(1)

gemini_api_url = os.getenv("GEMINI_API_URL")
if not gemini_api_url:
    print(
        "[red]Error:[/red] [green]GEMINI_API_URL[/green] is not set in the environment variables."
    )
    exit(1)

gemini_api_model = os.getenv("GEMINI_API_MODEL")
if not gemini_api_model:
    print(
        "[red]Error:[/red] [green]GEMINI_API_MODEL[/green] is not set in the environment variables."
    )
    exit(1)

class MySecrets:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = gemini_api_url
        self.gemini_api_model = gemini_api_model