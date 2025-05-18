from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_tracing_disabled,
    set_default_openai_client,
    set_default_openai_api,
)
from streaming_agent.my_secrets import Secrets
import asyncio
from rich import print
from openai.types.responses import ResponseTextDeltaEvent

secrets = Secrets()


async def custom_agent():

    external_cleint = AsyncOpenAI(
        base_url=secrets.gemini_api_url,
        api_key=secrets.gemini_api_key,
    )

    set_default_openai_client(external_cleint)
    set_default_openai_api("chat_completions")
    set_tracing_disabled(disabled=True)

    agent = Agent(
        name="streaming_agent",
        instructions="You respond in a conversational manner.",
        model=secrets.gemini_api_model,
    )

    result = Runner.run_streamed(
        starting_agent=agent,
        input="What is generative AI?",
    )
    
    ResponseTextDeltaEvent
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


def main():
    asyncio.run(custom_agent())