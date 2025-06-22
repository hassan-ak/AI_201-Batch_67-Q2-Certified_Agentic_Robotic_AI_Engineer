import chainlit as cl

from typing import cast

from agents import (
    Agent,
    Runner,
    RunConfig,
    AsyncOpenAI,
    set_default_openai_client,
    set_default_openai_api,
    set_tracing_disabled,
)
from input_guard import math_guardrail
from output_guard import math_output_guardrail
from my_secrets import Secrets

secrets = Secrets()


@cl.on_chat_start
async def start():

    external_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key, base_url=secrets.gemini_api_url
    )
    set_default_openai_client(external_client)
    set_default_openai_api("chat_completions")
    set_tracing_disabled(True)
    cl.user_session.set("chat_history", [])

    agent: Agent = Agent(
        name="Customer support agent",
        instructions="You are a customer support agent. You help customers with their questions.",
        input_guardrails=[math_guardrail],
        output_guardrails=[math_output_guardrail],
        model=secrets.gemini_api_model,
    )
    cl.user_session.set("agent", agent)

    await cl.Message(
        content="Welcome to the Panaversity AI Assistant! How can I help you today?"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    # Send a thinking message
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

    # Retrieve the chat history from the session.
    history = cl.user_session.get("chat_history") or []

    # Append the user's message to the history.
    history.append({"role": "user", "content": message.content})

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        result = Runner.run_sync(starting_agent=agent, input=history, run_config=config)

        print(f"RAW Result: {result}")
        response_content = result.final_output

        # Update the thinking message with the actual response
        msg.content = response_content
        await msg.update()

        # Update the session with the new history.
        cl.user_session.set("chat_history", result.to_input_list())

        # Optional: Log the interaction
        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
