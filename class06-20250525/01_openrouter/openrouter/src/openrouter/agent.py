from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from openrouter.secrets import secrets
from rich import print

external_client = AsyncOpenAI(
    api_key=secrets["OPENROUTER_API_KEY"],
    base_url=secrets["OPENROUTER_API_URL"],
)
set_tracing_disabled(True)

def agent_gemini():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(
            model=secrets["OPENROUTER_GEMINI_MODEL"],
            openai_client=external_client,
        ),
    )
    result = Runner.run_sync(
        agent, "Can we travel back in time, respond in a couple of lines?"
    )
    print("\n")
    print(result.final_output)
    print("\n")


def agent_deepseek():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=OpenAIChatCompletionsModel(
            model=secrets["OPENROUTER_DEEPSEEK_MODEL"],
            openai_client=external_client,
        ),
    )
    result = Runner.run_sync(
        agent, "What is butterfly effect, respond in a couple of lines?"
    )
    print("\n")
    print(result.final_output)
    print("\n")
