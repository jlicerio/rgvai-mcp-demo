# todo-demo MCP Server

MCP server for todo-demo (CLI application, with 9 capabilities)

## Available Tools

Status meanings:
- `ready`: fully generated, no manual steps required
- `scaffolded`: generated code needs manual wiring before use
- `stubbed`: no implementation was generated

### run_todo_demo

Run todo-demo with the given command-line arguments

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Run: python todo.py <args>`

Parameters:
- `args` (string): Command-line arguments to pass to todo-demo (e.g. a URL or flags)
### add

Add a task

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py`

Parameters:
- `text` (string): Task description
### clear

Delete all tasks

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py`

Parameters:
- `args` (string, optional): Arguments for clear
### delete

Delete a task

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py`

Parameters:
- `id` (integer): Task ID
### done

Mark a task as done

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py`

Parameters:
- `id` (integer): Task ID
### list

List all tasks

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py`

Parameters:
- `args` (string, optional): Arguments for list
### cmd_add

Cmd add

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py::cmd_add`

Parameters:
- `args` (string): 
### cmd_clear

Cmd clear

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py::cmd_clear`

Parameters:
- `args` (string): 
### cmd_list

Cmd list

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py::cmd_list`

Parameters:
- `args` (string): 
### save_tasks

Save tasks

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: todo.py::save_tasks`

Parameters:
- `tasks` (string): 

## Available Resources

- `app://todo-demo/status` — Current status and version of todo-demo
- `app://todo-demo/commands` — Available commands and tools in todo-demo
- `docs://todo-demo/tool-index` — Complete index of all todo-demo tools with parameters and usage
- `docs://todo-demo/cli_command` — Documentation for todo-demo cli_command capabilities
- `docs://todo-demo/file_ops` — Documentation for todo-demo file_ops capabilities

## Available Prompts

- `use_todo_demo` — Guide for using todo-demo tools effectively
- `debug_todo_demo` — Diagnose issues with todo-demo operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "todo-demo": {
      "command": "mcp-todo-demo"
    }
  }
}
```
