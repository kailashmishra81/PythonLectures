import asyncio
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_agentchat.ui import Console

os.environ["OPENAI_API_KEY"] = "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"

async def main():
    fs_root = "C:/Users/PRIYANKA/Documents/AssistantFiles"

    fs_server_params = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            fs_root
        ],
        cwd=fs_root  # 🔥 THIS IS THE FIX
    )


    workbench = McpWorkbench(fs_server_params)
    await workbench.start()

    try:
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

        assistant = AssistantAgent(
            name="assistant_fs",
            model_client=model_client,
            workbench=workbench,
            system_message=(
                "You can read and write files ONLY inside the filesystem root. "
   #             "Always use relative paths starting with './'."
            )
        )

        await Console(
            assistant.run_stream(
                task=(
                    "Explain what is AI agentic solution with MCP and AutoGEN and save the explanation to './result.txt'."
                ),
   #             cancellation_token=CancellationToken()
            )
        )

    finally:
        await workbench.stop()

asyncio.run(main())
