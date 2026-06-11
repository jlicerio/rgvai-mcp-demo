"""Resources for textutils-demo."""

import json

from mcp.server.fastmcp import FastMCP

_TOOL_METADATA = {
    "run_textutils_demo": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Run: python textutils.py \u003cargs\u003e",
        "manual_steps": [],
    },
    "palindrome": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py",
        "manual_steps": [],
    },
    "checksum": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::checksum",
        "manual_steps": [],
    },
    "count": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::count",
        "manual_steps": [],
    },
    "lowercase": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::lowercase",
        "manual_steps": [],
    },
    "reverse": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::reverse",
        "manual_steps": [],
    },
    "slugify": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::slugify",
        "manual_steps": [],
    },
    "uppercase": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: textutils.py::uppercase",
        "manual_steps": [],
    },
}


def register_resources(server: FastMCP, _get_backend) -> None:
    """Register resources with the server."""

    @server.resource("app://textutils-demo/status")
    async def textutils_demo_status() -> str:
        """Current status and version of textutils-demo"""
        try:
            version = await _get_backend().run_cli(["--version"])
        except Exception:
            version = "unknown"
        return json.dumps({
            "name": "textutils-demo",
            "version": version.strip(),
            "status": "running",
            "tool_generation": {
                "ready": 8,
                "proxy": 0,
                "scaffolded": 0,
                "stubbed": 0,
            },
        }, indent=2)

    @server.resource("app://textutils-demo/commands")
    async def textutils_demo_commands() -> str:
        """Available commands and tools in textutils-demo"""
        tools = await server.list_tools()
        commands = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            commands.append({
                "name": tool.name,
                "description": tool.description or "",
                "generation_status": metadata.get("generation_status", "ready"),
                "generation_notes": metadata.get("generation_notes", ""),
                "manual_steps": metadata.get("manual_steps", []),
            })
        return json.dumps({"commands": commands}, indent=2)

    @server.resource("docs://textutils-demo/tool-index")
    async def textutils_demo_tool_index() -> str:
        """Complete index of all textutils-demo tools with parameters and usage"""
        # Dynamic documentation resource
        tools = await server.list_tools()
        doc_entries = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            entry["generation_status"] = metadata.get("generation_status", "ready")
            entry["generation_notes"] = metadata.get("generation_notes", "")
            entry["implementation_hint"] = metadata.get("implementation_hint", "")
            entry["manual_steps"] = metadata.get("manual_steps", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "textutils-demo",
            "resource": "docs://textutils-demo/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://textutils-demo/cli_command")
    async def textutils_demo_cli_command_docs() -> str:
        """Documentation for textutils-demo cli_command capabilities"""
        # Dynamic documentation resource
        tools = await server.list_tools()
        doc_entries = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            entry["generation_status"] = metadata.get("generation_status", "ready")
            entry["generation_notes"] = metadata.get("generation_notes", "")
            entry["implementation_hint"] = metadata.get("implementation_hint", "")
            entry["manual_steps"] = metadata.get("manual_steps", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "textutils-demo",
            "resource": "docs://textutils-demo/cli_command",
            "tools": doc_entries,
        }, indent=2)

