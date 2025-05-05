from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from agent_hello.secrets import secrets
from rich import print

external_client = AsyncOpenAI(
    api_key=secrets["GEMINI_API_KEY"],
    base_url=secrets["GEMINI_API_URL"],
)
set_tracing_disabled(True)


def main():
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
        model=OpenAIChatCompletionsModel(
            model=secrets["GEMINI_API_MODEL"],
            openai_client=external_client,
        ),
    )
    result = Runner.run_sync(agent, "What is GenAI, respond in couple lines?")
    print("\n")
    print(result.final_output)
