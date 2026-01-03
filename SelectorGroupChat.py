import asyncio
import os

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMessageTermination, TextMentionTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat

from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

os.environ[
    "OPENAI_API_KEY"]="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"
async def main1():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    Reporter_Pakistan= AssistantAgent(name="Reporter_Pakistan",model_client=model_client,system_message="You are a Pakistani reporter and have expertise in reporting news of Pakistan .Explain your views")

    Reporter_India = AssistantAgent(name="Reporter_India", model_client=model_client,
                         system_message="You are a Indian reporter and have expertise in reporting news of India .Explain your views")


    Kashmiri_Citizen = AssistantAgent(name="Kashmiri_Citizen", model_client=model_client,
                         system_message="You are a Kashmiri citizen . Explain your views and the problems people of Kashmir faced.")

    critic = AssistantAgent(name="Critic", model_client=model_client,
                         system_message="You are playing the role of a critic on this topic.Hear the opinions of all the parties and also share your views in terms of the operation SINDOOR. Say OK if you are fine with producing this operation been executed or it would have been fine if the plan was executed in a different fashion")

    termination = TextMentionTermination("TERMINATE")
    max_messages_termination=MaxMessageTermination(max_messages=15)
    terminate=termination | max_messages_termination
    team = SelectorGroupChat(
        [Reporter_Pakistan,Reporter_India,Kashmiri_Citizen,critic],
        model_client=model_client,
        termination_condition=terminate)

    stream = team.run_stream(task="We are discussing on the Pahalgam attack happened on April 22nd 2025 and on the topic Operation SINDOOR")
    await Console(stream)
    await model_client.close()

asyncio.run(main1())


