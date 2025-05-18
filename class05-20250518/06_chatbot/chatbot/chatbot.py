import chainlit as cl
from my_secrets import Secrets
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled,
)


@cl.on_message
async def main(message: cl.Message):

    secrets = Secrets()

    external_client = AsyncOpenAI(
        base_url=secrets.gemini_api_url,
        api_key=secrets.gemini_api_key,
    )
    set_default_openai_client(external_client)
    set_default_openai_api("chat_completions")
    set_tracing_disabled(True)

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        model=secrets.gemini_api_model,
    )

    result = Runner.run_sync(
        agent,
        "Hello, how can I assist you today?",
    )

    await cl.Message(
        content=result.final_output,
    ).send()
