# calculator-demo MCP Server

MCP server for calculator-demo (CLI application, with 5 capabilities)

## Available Tools

Status meanings:
- `ready`: fully generated, no manual steps required
- `scaffolded`: generated code needs manual wiring before use
- `stubbed`: no implementation was generated

### run_calculator_demo

Run calculator-demo with the given command-line arguments

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Run: python calculator.py <args>`

Parameters:
- `args` (string): Command-line arguments to pass to calculator-demo (e.g. a URL or flags)
### clear

Clear calculation history

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: calculator.py`

Parameters:
- `args` (string, optional): Arguments for clear
### history

Show calculation history

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: calculator.py`

Parameters:
- `args` (string, optional): Arguments for history
### sqrt

Square root

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: calculator.py`

Parameters:
- `a` (string): Number
### record_operation

Record operation

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: calculator.py::record_operation`

Parameters:
- `op` (string): 
- `a` (string): 
- `b` (string): 
- `result` (string): 
### save_history

Save history

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: calculator.py::save_history`

Parameters:
- `entries` (string): 

## Available Resources

- `app://calculator-demo/status` — Current status and version of calculator-demo
- `app://calculator-demo/commands` — Available commands and tools in calculator-demo
- `docs://calculator-demo/tool-index` — Complete index of all calculator-demo tools with parameters and usage
- `docs://calculator-demo/cli_command` — Documentation for calculator-demo cli_command capabilities
- `docs://calculator-demo/file_ops` — Documentation for calculator-demo file_ops capabilities

## Available Prompts

- `use_calculator_demo` — Guide for using calculator-demo tools effectively
- `debug_calculator_demo` — Diagnose issues with calculator-demo operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "calculator-demo": {
      "command": "mcp-calculator-demo"
    }
  }
}
```
