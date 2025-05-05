from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_api
)
from agent_hello.secrets import secrets


external_client = AsyncOpenAI(
    api_key=secrets["GEMINI_API_KEY"],
    base_url=secrets["GEMINI_API_URL"],
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

def main():
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model=secrets["GEMINI_API_MODEL"],
    )
    result = Runner.run_sync(agent, "How are you?")
    print("\n")
    print(result.final_output)
    
