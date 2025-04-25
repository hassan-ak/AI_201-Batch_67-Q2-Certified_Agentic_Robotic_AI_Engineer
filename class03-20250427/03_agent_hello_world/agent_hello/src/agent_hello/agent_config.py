import os
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_tracing_disabled(True)


def main():
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=external_client,
        ),
    )
    result = Runner.run_sync(agent, "What is GenAI, respond in couple lines?")
    print("\n")
    print(result.final_output)
    print("\n")
