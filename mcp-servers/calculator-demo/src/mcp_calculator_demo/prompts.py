"""Server-delivered MCP prompts (skills) for calculator-demo."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_calculator_demo")
    async def use_calculator_demo_prompt() -> str:
        """Guide for using calculator-demo tools effectively"""
        return """You have access to the calculator-demo MCP server with these tools:

- clear: Clear calculation history
- history: Show calculation history
- sqrt: Square root
- record_operation: Record operation
- save_history: Save history

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_calculator_demo")
    async def debug_calculator_demo_prompt(error_message: str) -> str:
        """Diagnose issues with calculator-demo operations"""
        return """The user encountered an error while using calculator-demo.

Error: {{error_message}}

Available tools: clear, history, sqrt, record_operation, save_history

Diagnose the issue and suggest which tool to use to resolve it."""

