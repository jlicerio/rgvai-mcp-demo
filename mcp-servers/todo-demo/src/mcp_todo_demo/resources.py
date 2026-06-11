"""Resources for todo-demo."""

import json

from mcp.server.fastmcp import FastMCP

_TOOL_METADATA = {
    "run_todo_demo": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Run: python todo.py \u003cargs\u003e",
        "manual_steps": [],
    },
    "add": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py",
        "manual_steps": [],
    },
    "clear": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py",
        "manual_steps": [],
    },
    "delete": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py",
        "manual_steps": [],
    },
    "done": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py",
        "manual_steps": [],
    },
    "list": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py",
        "manual_steps": [],
    },
    "cmd_add": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py::cmd_add",
        "manual_steps": [],
    },
    "cmd_clear": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py::cmd_clear",
        "manual_steps": [],
    },
    "cmd_list": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py::cmd_list",
        "manual_steps": [],
    },
    "save_tasks": {
        "generation_status": "ready",
        "generation_notes": "Invokes the detected CLI entry point.",
        "implementation_hint": "Source: todo.py::save_tasks",
        "manual_steps": [],
    },
}


def register_resources(server: FastMCP, _get_backend) -> None:
    """Register resources with the server."""

    @server.resource("app://todo-demo/status")
    async def todo_demo_status() -> str:
        """Current status and version of todo-demo"""
        try:
            version = await _get_backend().run_cli(["--version"])
        except Exception:
            version = "unknown"
        return json.dumps({
            "name": "todo-demo",
            "version": version.strip(),
            "status": "running",
            "tool_generation": {
                "ready": 10,
                "proxy": 0,
                "scaffolded": 0,
                "stubbed": 0,
            },
        }, indent=2)

    @server.resource("app://todo-demo/commands")
    async def todo_demo_commands() -> str:
        """Available commands and tools in todo-demo"""
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

    @server.resource("docs://todo-demo/tool-index")
    async def todo_demo_tool_index() -> str:
        """Complete index of all todo-demo tools with parameters and usage"""
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
            "server": "todo-demo",
            "resource": "docs://todo-demo/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://todo-demo/cli_command")
    async def todo_demo_cli_command_docs() -> str:
        """Documentation for todo-demo cli_command capabilities"""
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
            "server": "todo-demo",
            "resource": "docs://todo-demo/cli_command",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://todo-demo/file_ops")
    async def todo_demo_file_ops_docs() -> str:
        """Documentation for todo-demo file_ops capabilities"""
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
            "server": "todo-demo",
            "resource": "docs://todo-demo/file_ops",
            "tools": doc_entries,
        }, indent=2)

