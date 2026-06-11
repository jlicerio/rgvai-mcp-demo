"""Server-delivered MCP prompts (skills) for weather-demo."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_weather_demo")
    async def use_weather_demo_prompt() -> str:
        """Guide for using weather-demo tools effectively"""
        return """You have access to the weather-demo MCP server with these tools:

- compare: Compare weather between two cities
- current: Show current weather for a city
- forecast: Show multi-day forecast for a city
- cmd_compare: Cmd compare
- cmd_current: Cmd current
- cmd_forecast: Cmd forecast

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_weather_demo")
    async def debug_weather_demo_prompt(error_message: str) -> str:
        """Diagnose issues with weather-demo operations"""
        return """The user encountered an error while using weather-demo.

Error: {{error_message}}

Available tools: compare, current, forecast, cmd_compare, cmd_current, cmd_forecast

Diagnose the issue and suggest which tool to use to resolve it."""

