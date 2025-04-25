from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
)
from dotenv import load_dotenv
from agents.run import RunConfig
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)


def main():
    agent = Agent(
        name="Assistant",
        instructions="A helpful assistant that can answer questions and provide information.",
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True,
    )

    result = Runner.run_sync(agent, "What is capital of Pakistan?", run_config=config)

    print("\n")
    print(result.final_output)
    print("\n")
