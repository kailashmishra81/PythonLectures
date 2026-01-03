import asyncio
import os

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_agentchat.ui import Console

os.environ["OPENAI_API_KEY"] = "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"
async def main():
    # Create the model client
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

    # Create a cancellation token
    cancellation_token = CancellationToken()

    # Create the assistant
    assistant = AssistantAgent(
        name="demo_agent",
        model_client=model_client,
        system_message="Explain a math problem."
    )

    # Start the assistant task in the background
    task = asyncio.create_task(
        Console(
            assistant.run_stream(
                task="Explain (3 + 5) * 12 in detail.",
                cancellation_token=cancellation_token
            )
        )
    )

    # Wait a few seconds, then cancel
    await asyncio.sleep(2)
    print("Cancelling the task...")
    cancellation_token.cancel()  # 🔥 trigger cancellation

    # Wait for the task to finish
    await task

asyncio.run(main())
