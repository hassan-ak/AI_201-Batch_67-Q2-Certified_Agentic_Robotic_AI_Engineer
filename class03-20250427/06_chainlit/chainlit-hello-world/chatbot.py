import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(
        content=f"Message Recieved: {message.content}",
    ).send()