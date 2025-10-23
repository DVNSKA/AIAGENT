# client_agent.py
import asyncio
from mcp.server.fastmcp import FastMCP
from agents import Agent, Runner, trace
from contextlib import asynccontextmanager
from rich.markdown import Markdown
from rich.console import Console
from agents.mcp import MCPServerStdio
console = Console()

# Define the instructions your agent should follow
instructions = """
You are an instructor agent for the MCP system.
You can invoke the following tools:
1. send_email(receiver_email, subject, text_body)
2. apply_leave(start_day, end_day)
3. generate_mom(path)

Answer the user queries by calling the appropriate MCP tool.
Ask for missing parameters if the user input is incomplete.
"""

# Example model, replace with the model your MCP uses
model = "gpt-4o-mini"  

async def main():
    # Optional params for MCPServerStdio
    params = {"command": "uv", "args": ["run","server.py"]}

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        # Create the agent
        agent = Agent(
            name="instructor_agent",
            instructions=instructions,
            model=model,
            mcp_servers=[mcp_server]
        )

        console.print("[bold green]Instructor Agent Ready![/bold green]")
        
        while True:
            # Get user request
            user_request = input("\nEnter your request (or 'exit' to quit): ").strip()
            if user_request.lower() == "exit":
                break

            # Run the agent
            with console.status("Processing...", spinner="dots"):
                result = await Runner.run(agent, user_request)

            # Display the output nicely
            console.print(Markdown(result.final_output))

if __name__ == "__main__":
    asyncio.run(main())
