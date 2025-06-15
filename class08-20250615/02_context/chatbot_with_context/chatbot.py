import os
from dotenv import load_dotenv
from typing import cast, List
import chainlit as cl
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    function_tool,
    set_default_openai_api,
)
from agents.run import RunConfig
from agents.tool import function_tool
from agents.run_context import RunContextWrapper
from dataclasses import dataclass
from my_secrets import Secrets

secrets = Secrets()

load_dotenv()


@cl.set_starters  # type: ignore
async def set_starts() -> List[cl.Starter]:
    return [
        cl.Starter(
            label="Author details",
            message="Can you share author details?",
        ),
    ]


@dataclass
class Developer:
    name: str
    city: str
    country: str


@function_tool
def get_author_details(wrapper: RunContextWrapper[Developer]):
    return f"The developer is {wrapper.context.name}, based in {wrapper.context.city}, {wrapper.context.country}."


@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key,
        base_url=secrets.gemini_api_url,
    )
    
    set_default_openai_client(external_client)
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")

    cl.user_session.set("chat_history", [])

    agent: Agent = Agent[Developer](
        name="Assistant",
        tools=[get_author_details],
        instructions="A helpful weather assistant, In case one ask for developer details use the respective tool.",
        model=secrets.gemini_api_model,
    )

    cl.user_session.set("agent", agent)


@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    
    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    developer = Developer(city="Tokyo", country="Japan", name="John Doe")

    try:
        result = Runner.run_sync(agent, history, context=developer, )

        response_content = result.final_output

        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
