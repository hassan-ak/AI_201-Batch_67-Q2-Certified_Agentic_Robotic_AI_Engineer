from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from dotenv import load_dotenv
import os
import asyncio


async def main():
    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client,
    )

    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model=model,
    )
    result = await Runner.run(agent, "What is capital of Farance?")
    print(result.final_output)
    
    
def run_main():
    asyncio.run(main())