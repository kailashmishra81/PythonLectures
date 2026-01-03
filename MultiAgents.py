import asyncio
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
    assistant1= AssistantAgent(name="AssistantAgent_Teacher",model_client=model_client,system_message="You are a Maths teacher.Explain concepts clearly and ask follow up questions")
    assistant2=AssistantAgent(name="AssistantAgent_Student",model_client=model_client,system_message="You are a Maths student.Ask questions related to the topic")
    Teams=RoundRobinGroupChat(participants=[assistant1,assistant2],termination_condition=MaxMessageTermination(6))

    stream = Teams.run_stream(task="Lets discuss about how Addition works?")
    await Console(stream)
    await model_client.close()

asyncio.run(main1())


