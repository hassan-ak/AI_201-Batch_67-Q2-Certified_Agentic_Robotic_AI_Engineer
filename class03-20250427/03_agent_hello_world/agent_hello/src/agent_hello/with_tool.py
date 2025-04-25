from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    function_tool,
)
from dotenv import load_dotenv
import os

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


@function_tool
def get_weather(city: str):
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


def main():

    agent = Agent(
        name="Assistant",
        instructions="A helpful weather assistant that can answer questions and provide information about the weather.",
        model=model,
        tools=[get_weather],
    )
    result = Runner.run_sync(agent, "What's the weather in Tokyo?")
    
    print("\n")
    print(result.final_output)
    print("\n")
    
