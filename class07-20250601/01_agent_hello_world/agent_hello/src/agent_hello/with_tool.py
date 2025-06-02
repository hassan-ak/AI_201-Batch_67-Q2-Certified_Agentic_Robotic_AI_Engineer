from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    set_tracing_disabled,
    function_tool,
    set_default_openai_api
)
from agent_hello.secrets import secrets
from rich import print

external_client = AsyncOpenAI(
    api_key=secrets["GEMINI_API_KEY"],
    base_url=secrets["GEMINI_API_URL"],
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")


@function_tool
def get_weather(city: str):
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


def main():

    agent = Agent(
        name="Assistant",
        instructions="A helpful weather assistant that can answer questions and provide information about the weather.",
        model=secrets["GEMINI_API_MODEL"],
        tools=[get_weather],
    )
    result = Runner.run_sync(agent, "What's the weather in Tokyo?")
    
    print("\n")
    print(result.final_output)
    
