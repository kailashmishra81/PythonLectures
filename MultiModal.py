import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage

from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"]="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"
async def main1():
    print("Hello World")

    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant= AssistantAgent(name="AssistantAgent_Kailash",model_client=model_client)
    image = Image.from_file(r"D:\1st Durga Pooja in Siliguri\IMG20201026145106.jpg")

    task=MultiModalMessage(source="user",
    content=["What do you see in this image?",image])

    stream = assistant.run_stream(task=task)
    await Console(stream)
    await model_client.close()

asyncio.run(main1())


