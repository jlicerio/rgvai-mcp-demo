"""Server-delivered MCP prompts (skills) for todo-demo."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_todo_demo")
    async def use_todo_demo_prompt() -> str:
        """Guide for using todo-demo tools effectively"""
        return """You have access to the todo-demo MCP server with these tools:

- add: Add a task
- clear: Delete all tasks
- delete: Delete a task
- done: Mark a task as done
- list: List all tasks
- cmd_add: Cmd add
- cmd_clear: Cmd clear
- cmd_list: Cmd list
- save_tasks: Save tasks

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_todo_demo")
    async def debug_todo_demo_prompt(error_message: str) -> str:
        """Diagnose issues with todo-demo operations"""
        return """The user encountered an error while using todo-demo.

Error: {{error_message}}

Available tools: add, clear, delete, done, list, cmd_add, cmd_clear, cmd_list, save_tasks

Diagnose the issue and suggest which tool to use to resolve it."""

