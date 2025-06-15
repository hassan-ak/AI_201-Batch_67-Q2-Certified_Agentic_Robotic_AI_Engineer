from agents import (
    Agent,
    Runner,
    set_default_openai_client,
    AsyncOpenAI,
    set_tracing_disabled,
    function_tool,
    set_default_openai_api,
    RunContextWrapper
)
from agent_with_context.my_secrets import Secrets
from rich import print
from dataclasses import dataclass

secrets = Secrets()

external_client = AsyncOpenAI(
    api_key=secrets.gemini_api_key,
    base_url=secrets.gemini_api_url,
)

set_default_openai_client(external_client)
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

@dataclass
class Developer:
    name: str
    city: str
    country: str


@function_tool
def get_author_details(wrapper: RunContextWrapper[Developer]):
    return f"The developer is {wrapper.context.name}, based in {wrapper.context.city}, {wrapper.context.country}."


def main():

    agent = Agent[Developer](
        name="Assistant",
        instructions="A helpful weather assistant, In case one ask for developer details use the respective tool.",
        model=secrets.gemini_api_model,
        tools=[get_author_details],
    )
    
    author = Developer(
        name="John Doe",
        city="Tokyo",
        country="Japan"
    )
    
    result = Runner.run_sync(agent, "Who is the author?", context=author)
    
    print("\n")
    print(result.final_output)
    
