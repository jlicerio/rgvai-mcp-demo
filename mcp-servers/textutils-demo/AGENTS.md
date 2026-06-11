# textutils-demo MCP Server

MCP server for textutils-demo (CLI application, with 7 capabilities)

## Available Tools

Status meanings:
- `ready`: fully generated, no manual steps required
- `scaffolded`: generated code needs manual wiring before use
- `stubbed`: no implementation was generated

### run_textutils_demo

Run textutils-demo with the given command-line arguments

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Run: python textutils.py <args>`

Parameters:
- `args` (string): Command-line arguments to pass to textutils-demo (e.g. a URL or flags)
### palindrome

check if text is a palindrome

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py`

Parameters:
- `text` (string): Text to check
### checksum

Compute SHA-256 checksum of text.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::checksum`

Parameters:
- `text` (string): 
### count

Count characters, words, and lines in text.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::count`

Parameters:
- `text` (string): 
### lowercase

Convert text to lowercase.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::lowercase`

Parameters:
- `text` (string): 
### reverse

Reverse the input string.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::reverse`

Parameters:
- `text` (string): 
### slugify

Convert text to a URL-friendly slug.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::slugify`

Parameters:
- `text` (string): 
### uppercase

Convert text to uppercase.

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: textutils.py::uppercase`

Parameters:
- `text` (string): 

## Available Resources

- `app://textutils-demo/status` — Current status and version of textutils-demo
- `app://textutils-demo/commands` — Available commands and tools in textutils-demo
- `docs://textutils-demo/tool-index` — Complete index of all textutils-demo tools with parameters and usage
- `docs://textutils-demo/cli_command` — Documentation for textutils-demo cli_command capabilities

## Available Prompts

- `use_textutils_demo` — Guide for using textutils-demo tools effectively
- `debug_textutils_demo` — Diagnose issues with textutils-demo operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "textutils-demo": {
      "command": "mcp-textutils-demo"
    }
  }
}
```
