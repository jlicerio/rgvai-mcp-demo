"""MCP server for todo-demo."""

import os

from mcp.server.fastmcp import FastMCP

server = FastMCP("todo-demo")


from mcp_todo_demo.backend import Backend

_backend: Backend | None = None


def _get_backend() -> Backend:
    """Lazily initialize the backend on first use."""
    global _backend
    if _backend is None:
        _backend = Backend()
    return _backend

# Import and register tool modules
from mcp_todo_demo.tools.general import register_tools as register_general_tools
register_general_tools(server, _get_backend)
from mcp_todo_demo.tools.cli_command import register_tools as register_cli_command_tools
register_cli_command_tools(server, _get_backend)
from mcp_todo_demo.tools.file_ops import register_tools as register_file_ops_tools
register_file_ops_tools(server, _get_backend)

# Import and register resources
from mcp_todo_demo.resources import register_resources
register_resources(server, _get_backend)

# Import and register prompts
from mcp_todo_demo.prompts import register_prompts
register_prompts(server)


def main():
    """Run the MCP server."""
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "http":
        host = os.environ.get("MCP_HOST", "0.0.0.0")
        port = int(os.environ.get("MCP_PORT", "8000"))
        server.settings.host = host
        server.settings.port = port
        server.run(transport="streamable-http")
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
