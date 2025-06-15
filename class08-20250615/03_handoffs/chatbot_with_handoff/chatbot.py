from typing import cast
import chainlit as cl
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    handoff,
    RunContextWrapper,
    set_tracing_disabled
)
from my_secrets import Secrets

secrets = Secrets()


@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key,
        base_url=secrets.gemini_api_url,
    )
    
    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model=secrets.gemini_api_model, openai_client=external_client
    )

    def on_handoff(agent: Agent, ctx: RunContextWrapper[None]):
        agent_name = agent.name
        print(f"Handing off to {agent_name}...")
        # Send a more visible message in the chat
        cl.Message(
            content=f"🔄 **Handing off to {agent_name}...**\n\nI'm transferring your request to our {agent_name.lower()} who will be able to better assist you.",
            author="System",
        ).send()

    billing_agent = Agent(
        name="Billing Agent", instructions="You are a billing agent", model=model
    )
    refund_agent = Agent(
        name="Refund Agent", instructions="You are a refund agent", model=model
    )

    # Correct on_handoff function definition

    agent = Agent(
        name="Triage Agent",
        instructions="You are a triage agent",
        model=model,
        handoffs=[
            handoff(
                billing_agent, on_handoff=lambda ctx: on_handoff(billing_agent, ctx)
            ),
            handoff(refund_agent, on_handoff=lambda ctx: on_handoff(refund_agent, ctx)),
        ],
    )

    # Set session variables
    cl.user_session.set("agent", agent)
    cl.user_session.set("chat_history", [])

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

    # Retrieve the chat history from the session.
    history = cl.user_session.get("chat_history") or []

    # Append the user's message to the history.
    history.append({"role": "user", "content": message.content})

    try:
        result = Runner.run_sync(agent, history)

        response_content = result.final_output

        # Update the thinking message with the actual response
        msg.content = response_content
        await msg.send()

        # IMPORTANT FIX HERE: use "developer" instead of "assistant"
        history.append({"role": "developer", "content": response_content})

        # Update session history
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
