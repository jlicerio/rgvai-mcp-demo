"""Resources for calculator-demo."""

import json

from mcp.server.fastmcp import FastMCP

_TOOL_METADATA = {
    "run_calculator_demo": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Run: python calculator.py \u003cargs\u003e",
        "manual_steps": [],
    },
    "clear": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: calculator.py",
        "manual_steps": [],
    },
    "history": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: calculator.py",
        "manual_steps": [],
    },
    "sqrt": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: calculator.py",
        "manual_steps": [],
    },
    "record_operation": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: calculator.py::record_operation",
        "manual_steps": [],
    },
    "save_history": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: calculator.py::save_history",
        "manual_steps": [],
    },
}


def register_resources(server: FastMCP, _get_backend) -> None:
    """Register resources with the server."""

    @server.resource("app://calculator-demo/status")
    async def calculator_demo_status() -> str:
        """Current status and version of calculator-demo"""
        try:
            version = await _get_backend().run_cli(["--version"])
        except Exception:
            version = "unknown"
        return json.dumps({
            "name": "calculator-demo",
            "version": version.strip(),
            "status": "running",
            "tool_generation": {
                "ready": 6,
                "proxy": 0,
                "scaffolded": 0,
                "stubbed": 0,
            },
        }, indent=2)

    @server.resource("app://calculator-demo/commands")
    async def calculator_demo_commands() -> str:
        """Available commands and tools in calculator-demo"""
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

    @server.resource("docs://calculator-demo/tool-index")
    async def calculator_demo_tool_index() -> str:
        """Complete index of all calculator-demo tools with parameters and usage"""
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
            "server": "calculator-demo",
            "resource": "docs://calculator-demo/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://calculator-demo/cli_command")
    async def calculator_demo_cli_command_docs() -> str:
        """Documentation for calculator-demo cli_command capabilities"""
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
            "server": "calculator-demo",
            "resource": "docs://calculator-demo/cli_command",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://calculator-demo/file_ops")
    async def calculator_demo_file_ops_docs() -> str:
        """Documentation for calculator-demo file_ops capabilities"""
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
            "server": "calculator-demo",
            "resource": "docs://calculator-demo/file_ops",
            "tools": doc_entries,
        }, indent=2)

