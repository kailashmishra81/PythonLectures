import asyncio
import os
import json
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from autogen_agentchat.ui import Console

# =============================================================================
# CONFIG
# =============================================================================
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your OpenAI key

JIRA_URL = "https://kailasakailash.atlassian.net"
JIRA_USERNAME = "kailasa.kailash@gmail.com"
JIRA_API_TOKEN = "ATATT3xFfGF0ZB5k2kYwIODHVIT21OHgkqE3_CP48jtCM7KgWfsJTXMs2O8RE3UwAtEVkmpnQsCyeTqIlmGQQLluQziDLIacOj1318u_DSX6tbOIOb_7M4_3bEi7Q6asXnNm-7-YMajZFPG482lRXx1gI9SLM5E9YU8kQ0sNvg_4-Bp0IleFfp8=9289F6F5"  # Replace with your JIRA API token
JIRA_PROJECT = "CRED"

FS_ROOT = "C:/Users/PRIYANKA/Documents/AssistantFiles"
os.makedirs(FS_ROOT, exist_ok=True)

# =============================================================================
# TOOL FUNCTION
# =============================================================================
def search_jira_bugs(project_key: str) -> list:
    """Fetch all Bug issues from a Jira project using JQL API."""
    url = f"{JIRA_URL}/rest/api/3/search/jql"
    payload = {
        "jql": f'project = "{project_key}" AND issuetype = Bug',
        "fields": ["summary", "status", "assignee", "priority"],
        "maxResults": 50
    }

    response = requests.post(
        url,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        json=payload,
        auth=HTTPBasicAuth(JIRA_USERNAME, JIRA_API_TOKEN)
    )
    response.raise_for_status()
    data = response.json()

    results = []
    for issue in data.get("issues", []):
        fields = issue["fields"]
        results.append({
            "key": issue["key"],
            "summary": fields["summary"],
            "status": fields["status"]["name"],
            "assignee": fields["assignee"]["displayName"] if fields.get("assignee") else "Unassigned",
            "priority": fields["priority"]["name"] if fields.get("priority") else "None"
        })

    # Save results to JSON file in MCP root
    json_file_path = os.path.join(FS_ROOT, "jira_bugs.json")
    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    print(f"Saved {len(results)} Jira bug(s) to {json_file_path}")

    return results

# =============================================================================
# AUTOGEN AGENT + MCP WORKBENCH
# =============================================================================
async def main():
    print("=" * 70)
    print("JIRA AGENT – AUTOGEN (TABLE OUTPUT via MCP Workbench)")
    print("=" * 70)

    # Step 1: Fetch Jira bugs and save JSON
    bugs = search_jira_bugs(JIRA_PROJECT)
    if not bugs:
        print("No bugs found in the project.")
        return

    # Step 2: Configure MCP Workbench
    fs_server_params = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            FS_ROOT
        ],
        cwd=FS_ROOT
    )

    workbench = McpWorkbench(fs_server_params)
    await workbench.start()

    try:
        # Step 3: Create assistant with Workbench
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
        assistant = AssistantAgent(
            name="JiraAssistant",
            model_client=model_client,
            workbench=workbench,
            system_message=(
                "You are a Jira QA assistant.\n"
                "You can read/write files ONLY inside the filesystem root.\n"
                "Read 'jira_bugs.json' and convert it into a clean table with columns:\n"
                "Key | Summary | Status | Assignee | Priority.\n"
                "Align columns neatly for console display. Do not output raw Python lists or JSON."
            )
        )

        # Step 4: Prompt assistant to read JSON and format table
        task_prompt = (
            "You have read the file './jira_bugs.json' from the MCP filesystem.\n"
            "The content is a JSON array of Jira bugs.\n"
            "Parse this JSON and convert it into a readable table with columns:\n"
            "Key | Summary | Status | Assignee | Priority.\n"
            "Print each bug on a new line and align columns neatly for console display.\n"
            "Do NOT print the raw JSON or Python lists."
        )

        await Console(
            assistant.run_stream(task=task_prompt)
        )

        # ---------- STEP 1: READ FILE ----------
        read_result = await assistant.run(
            task="Read './jira_bugs.json' and return its contents."
        )

        # json_text = None
        # for msg in reversed(read_result.messages):
        #     if msg.source == "JiraAssistant":
        #         json_text = msg.content
        #         break

        # ---------- STEP 2: FORCE TRANSFORMATION ----------
        table_task = (
            "Convert the JSON placed inside the filesystem into a readable ASCII table.\n"
            "Columns: Key | Summary | Status | Assignee | Priority.\n"
            "Align columns neatly for console output.\n\n"

        )

        table_result = await assistant.run(task=table_task)
        print(table_result)

    finally:
        await workbench.stop()


if __name__ == "__main__":
    asyncio.run(main())
