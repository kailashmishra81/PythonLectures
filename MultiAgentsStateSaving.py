import asyncio
import json
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"]="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"
async def main1():
    print("Hello World")

    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant1= AssistantAgent(name="AssistantAgent_Teacher",model_client=model_client)
    assistant2=AssistantAgent(name="AssistantAgent_Student",model_client=model_client)


    stream = assistant1.run_stream(task="My favourite colour is GREEN")
    await Console(stream)
    state= await assistant1.save_state()
    with open("mem.json", "w") as fp:
        json.dump(state, fp,default=str)
    with open("mem.json", "r") as fp:
        saved_state=json.load(fp)
    await assistant2.load_state(saved_state)
    stream = assistant2.run_stream(task="Earlier you were told that your favourite colour is RED. What is it?")

    await Console(stream)
    await model_client.close()

asyncio.run(main1())


