"""Resources for weather-demo."""

import json

from mcp.server.fastmcp import FastMCP

_TOOL_METADATA = {
    "run_weather_demo": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Run: python weather.py \u003cargs\u003e",
        "manual_steps": [],
    },
    "compare": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py",
        "manual_steps": [],
    },
    "current": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py",
        "manual_steps": [],
    },
    "forecast": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py",
        "manual_steps": [],
    },
    "cmd_compare": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py::cmd_compare",
        "manual_steps": [],
    },
    "cmd_current": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py::cmd_current",
        "manual_steps": [],
    },
    "cmd_forecast": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: weather.py::cmd_forecast",
        "manual_steps": [],
    },
}


def register_resources(server: FastMCP, _get_backend) -> None:
    """Register resources with the server."""

    @server.resource("app://weather-demo/status")
    async def weather_demo_status() -> str:
        """Current status and version of weather-demo"""
        try:
            version = await _get_backend().run_cli(["--version"])
        except Exception:
            version = "unknown"
        return json.dumps({
            "name": "weather-demo",
            "version": version.strip(),
            "status": "running",
            "tool_generation": {
                "ready": 7,
                "proxy": 0,
                "scaffolded": 0,
                "stubbed": 0,
            },
        }, indent=2)

    @server.resource("app://weather-demo/commands")
    async def weather_demo_commands() -> str:
        """Available commands and tools in weather-demo"""
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

    @server.resource("docs://weather-demo/tool-index")
    async def weather_demo_tool_index() -> str:
        """Complete index of all weather-demo tools with parameters and usage"""
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
            "server": "weather-demo",
            "resource": "docs://weather-demo/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://weather-demo/cli_command")
    async def weather_demo_cli_command_docs() -> str:
        """Documentation for weather-demo cli_command capabilities"""
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
            "server": "weather-demo",
            "resource": "docs://weather-demo/cli_command",
            "tools": doc_entries,
        }, indent=2)

