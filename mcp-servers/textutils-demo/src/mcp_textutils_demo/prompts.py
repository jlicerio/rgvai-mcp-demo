"""Server-delivered MCP prompts (skills) for textutils-demo."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_textutils_demo")
    async def use_textutils_demo_prompt() -> str:
        """Guide for using textutils-demo tools effectively"""
        return """You have access to the textutils-demo MCP server with these tools:

- palindrome: check if text is a palindrome
- checksum: Compute SHA-256 checksum of text.
- count: Count characters, words, and lines in text.
- lowercase: Convert text to lowercase.
- reverse: Reverse the input string.
- slugify: Convert text to a URL-friendly slug.
- uppercase: Convert text to uppercase.

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_textutils_demo")
    async def debug_textutils_demo_prompt(error_message: str) -> str:
        """Diagnose issues with textutils-demo operations"""
        return """The user encountered an error while using textutils-demo.

Error: {{error_message}}

Available tools: palindrome, checksum, count, lowercase, reverse, slugify, uppercase

Diagnose the issue and suggest which tool to use to resolve it."""

