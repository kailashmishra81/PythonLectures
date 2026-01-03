import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

os.environ[
    "OPENAI_API_KEY"]="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"

# Create output folder if it does not exist
os.makedirs("./outputs", exist_ok=True)

async def main():
    # Define MCP servers with mandatory 'command' parameter
    fs_server_params = StdioServerParams(
        name="Secure MCP Filesystem Server",
        command=["python", "-m", "autogen_ext.tools.mcp_filesystem_server"]
    )

    rest_server_params = StdioServerParams(
        name="REST API Tester MCP server",
        command=["python", "-m", "autogen_ext.tools.mcp_rest_server"]
    )

    # Start MCP workbench
    workbench = McpWorkbench(servers=[fs_server_params, rest_server_params])

    # Initialize assistant agent
    assistant = AssistantAgent(
        name="MCP Assistant",
        workbench=workbench,
        termination_conditions=[MaxMessageTermination(1)]
    )

    # Define the task for the assistant
    task_instruction = """
You have access to a Postman collection file named 'api_contract.json'.
Tasks:
1. Read the collection and understand the JSON schema for the /booking POST request.
2. Use the REST API MCP tool to perform a POST to '/booking' with the payload in the collection.
3. Retrieve the 'bookingid' from the POST response.
4. Use the REST API MCP tool to perform a GET request on '/booking/{bookingid}'.
5. Save the POST response to './outputs/post_response.json' and the GET response to './outputs/get_response.json'.
6. Ensure required headers (Content-Type, Accept, Custom-Client, X-API-Version) are automatically included.
Only show the final GET response JSON as output.
"""

    # Run the assistant
    response_messages = await assistant.run([TextMessage(role="user", content=task_instruction)])

    # Print the assistant's final response
    for msg in response_messages:
        print(msg.content)

if __name__ == "__main__":
    asyncio.run(main())
