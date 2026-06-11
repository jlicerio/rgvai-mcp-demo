# weather-demo MCP Server

MCP server for weather-demo (CLI application, with 6 capabilities)

## Available Tools

Status meanings:
- `ready`: fully generated, no manual steps required
- `scaffolded`: generated code needs manual wiring before use
- `stubbed`: no implementation was generated

### run_weather_demo

Run weather-demo with the given command-line arguments

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Run: python weather.py <args>`

Parameters:
- `args` (string): Command-line arguments to pass to weather-demo (e.g. a URL or flags)
### compare

Compare weather between two cities

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py`

Parameters:
- `city1` (string): First city
- `city2` (string): Second city
### current

Show current weather for a city

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py`

Parameters:
- `city` (string): City name
### forecast

Show multi-day forecast for a city

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py`

Parameters:
- `city` (string): City name
- `days` (integer, optional): Number of forecast days (default: 5)
### cmd_compare

Cmd compare

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py::cmd_compare`

Parameters:
- `args` (Namespace): 
### cmd_current

Cmd current

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py::cmd_current`

Parameters:
- `args` (Namespace): 
### cmd_forecast

Cmd forecast

Implementation status: `ready`
Notes: Invokes the detected CLI entry point.
Source hint: `Source: weather.py::cmd_forecast`

Parameters:
- `args` (Namespace): 

## Available Resources

- `app://weather-demo/status` — Current status and version of weather-demo
- `app://weather-demo/commands` — Available commands and tools in weather-demo
- `docs://weather-demo/tool-index` — Complete index of all weather-demo tools with parameters and usage
- `docs://weather-demo/cli_command` — Documentation for weather-demo cli_command capabilities

## Available Prompts

- `use_weather_demo` — Guide for using weather-demo tools effectively
- `debug_weather_demo` — Diagnose issues with weather-demo operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "weather-demo": {
      "command": "mcp-weather-demo"
    }
  }
}
```
