import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="This is a dummy response to your message.").send()
