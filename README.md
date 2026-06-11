# RGV AI — MCP Demo Suite

> **4 example apps + auto-generated MCP servers. Turn any CLI tool into an LLM-accessible tool — no boilerplate, no API wrappers, no manual networking.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![Node](https://img.shields.io/badge/node-18%2B-green)](#)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](#)

```
npx rgvai-mcp-demo            # interactive menu
pip install mcp-anything       # MCP server generator
mcp-anything generate ./demos/calculator  # wraps calculator.py as MCP server
```

---

## Quick Install

```bash
# Clone it
git clone https://github.com/jlicerio/rgvai-mcp-demo.git
cd rgvai-mcp-demo

# Install mcp-anything (the MCP server generator)
pip install mcp-anything

# Try the demos directly (no MCP needed to test)
python3 demos/calculator/calculator.py add 5 3
python3 demos/todo/todo.py add "Buy milk"
python3 demos/weather/weather.py current Austin

# Generate MCP servers for all demos
node bin/generate-all.js

# Open the interactive menu
npx mcp-demo
```

**Requirements:** Python 3.10+, Node.js 18+, an MCP-compatible client (Claude Desktop, VS Code + Cline, Cursor).

---

## What This Does

This project demonstrates **`mcp-anything`** — a tool that scans your source code and generates a complete MCP server automatically. You write normal CLI scripts. It builds the bridge to your LLM.

```
Your Code (calculator.py)      MCP Server (auto-generated)      LLM Client
┌──────────────────┐           ┌──────────────────────┐         ┌──────────┐
│  python3 calc.py │ ──mcp────▶│  add(a,b)            │──stdio──▶│  Claude  │
│  add 5 3         │  anything │  sqrt(value)         │          │  VS Code │
│                  │  generate │  history()            │          │  Cursor  │
└──────────────────┘           └──────────────────────┘         └──────────┘
```

---

## The 4 Demo Apps

| Demo | Script | Tools Generated | What It Shows |
|------|--------|----------------|---------------|
| 🧮 **calculator** | `demos/calculator/calculator.py` | add, subtract, multiply, divide, power, sqrt, history | CLI math ops, JSON history |
| ✅ **todo** | `demos/todo/todo.py` | add_task, list_tasks, done_task, delete_task, clear_tasks | CRUD, file persistence |
| 🌤 **weather** | `demos/weather/weather.py` | current_weather, forecast, compare_cities | Simulated API, formatted output |
| 📝 **textutils** | `demos/textutils/textutils.py` | count, reverse, uppercase, slugify, palindrome, checksum | String processing |

Test any of them directly:
```bash
python3 demos/textutils/textutils.py palindrome "racecar"
python3 demos/weather/weather.py compare Austin "San Antonio"
python3 demos/todo/todo.py add "Write workshop slides"
```

---

## Generate MCP Servers

### One at a time

```bash
mcp-anything generate ./demos/calculator --name calculator-demo --transport stdio -o ./mcp-servers/calculator-demo
mcp-anything generate ./demos/todo --name todo-demo --transport stdio -o ./mcp-servers/todo-demo
mcp-anything generate ./demos/weather --name weather-demo --transport stdio -o ./mcp-servers/weather-demo
mcp-anything generate ./demos/textutils --name textutils-demo --transport stdio -o ./mcp-servers/textutils-demo
```

### All at once

```bash
node bin/generate-all.js
```

Or via npm:
```bash
npm run generate
```

---

## Connect to Your LLM Client

Add to your MCP client config (Claude Desktop, VS Code with Cline, Cursor, Continue):

```json
{
  "mcpServers": {
    "calculator-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/calculator-demo"]
    },
    "todo-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/todo-demo"]
    },
    "weather-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/weather-demo"]
    },
    "textutils-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/textutils-demo"]
    }
  }
}
```

**Config locations by client:**

| Client | Config File |
|--------|------------|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| VS Code (Cline) | `.vscode/mcp.json` (project) or Cline global settings |
| Cursor | `~/.cursor/mcp.json` |
| Continue | `~/.continue/config.json` |
| Zed | `~/.config/zed/settings.json` |

---

## The 'Aha!' Moment

Once connected, ask your LLM:

> *"Use the calculator to add 25 and 17, multiply by 3, then divide by 6."*
> *"Add 'Buy milk' and 'Write docs' to my todo list, then show me what's pending."*
> *"What's the weather in Austin compared to McAllen?"*
> *"Check if 'racecar' is a palindrome, then reverse the word 'hello'."*

The LLM calls your local tools through MCP. It went from "brain in a jar" to actively driving your code.

---

## Pi (pi.dev) Coding Agent Setup

[Pi](https://pi.dev) is a terminal-based AI coding agent that supports MCP through the `pi-mcp-adapter` extension. Here's how to connect the demo MCP servers to Pi.

### Install pi-mcp-adapter

```bash
# Via Pi's built-in package manager (recommended)
pi install npm:pi-mcp-adapter

# Then restart Pi
```

The adapter auto-detects MCP config files at `~/.config/mcp/mcp.json`, `.mcp.json`, or any Cursor/Claude Code configs. If nothing is found, run `/mcp setup` inside Pi to scaffold one.

### Configure the Demo MCP Servers

Create or edit `~/.pi/agent/mcp.json` (or `.mcp.json` in your project directory):

```json
{
  "settings": {
    "directTools": true
  },
  "mcpServers": {
    "calculator-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/calculator-demo"]
    },
    "todo-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/todo-demo"]
    },
    "weather-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/weather-demo"]
    },
    "textutils-demo": {
      "command": "mcp-anything",
      "args": ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/textutils-demo"]
    }
  }
}
```

With `directTools: true`, each MCP tool becomes a first-class Pi command.

### Use the Demos in Pi

Once configured, just ask Pi:

```
pi> add 42 and 58 using the calculator
pi> add "Buy milk" to my todo list, then show me what's pending
pi> what's the weather in Austin?
pi> check if "racecar" is a palindrome
```

Pi's adapter is **token-efficient** — it uses a single proxy tool (~200 tokens) instead of loading all tool definitions upfront. Servers are **lazy** by default (connect on first use, disconnect after idle timeout).

### Proxy Mode

If `directTools` is off, use the `mcp` proxy tool:

```
pi> mcp({ tool: "add", args: '{"a": 5, "b": 3}' })
pi> mcp({ search: "calculator" })
pi> mcp({ server: "weather-demo" })
```

### Config File Locations (Precedence)

| File | Scope |
|------|-------|
| `~/.config/mcp/mcp.json` | User-global (shared) |
| `~/.pi/agent/mcp.json` | Pi-specific global |
| `.mcp.json` | Project-local (shared) |
| `.pi/mcp.json` | Pi project-specific |

---

## OpenCode CLI Setup

[OpenCode](https://opencode.ai) is an open-source terminal-based AI coding agent with built-in MCP support. Configure it to use the demo MCP servers.

### Configure the Demo MCP Servers

Add to `~/.config/opencode/opencode.json` (global) or `opencode.json` (project root):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "calculator-demo": {
      "type": "local",
      "command": ["mcp-anything", "serve", "/ABSOLUTE/PATH/TO/mcp-servers/calculator-demo"],
      "enabled": true
    },
    "todo-demo": {
      "type": "local",
      "command": ["mcp-anything", "serve", "/ABSOLUTE/PATH/TO/mcp-servers/todo-demo"],
      "enabled": true
    },
    "weather-demo": {
      "type": "local",
      "command": ["mcp-anything", "serve", "/ABSOLUTE/PATH/TO/mcp-servers/weather-demo"],
      "enabled": true
    },
    "textutils-demo": {
      "type": "local",
      "command": ["mcp-anything", "serve", "/ABSOLUTE/PATH/TO/mcp-servers/textutils-demo"],
      "enabled": true
    }
  }
}
```

Server options:

| Field | Description |
|-------|-------------|
| `command` | Command + args as an array (required for local) |
| `type` | `"local"` for stdio servers |
| `enabled` | Enable on startup (default: false) |
| `timeout` | Fetch timeout in ms (default: 5000) |
| `environment` | Optional env variables for the server |

### Use the Demos in OpenCode

Just ask in the OpenCode TUI or `opencode run`:

```
Use the calculator to add 42 and 58
Use the todo tool to add "Buy milk" to my list
Check the weather in Austin
```

### Managing MCP Servers

```bash
opencode mcp list              # List configured MCP servers
opencode mcp auth calculator-demo   # Authenticate (if needed)
opencode mcp logout calculator-demo # Remove credentials
```

### Config Precedence

| Priority | Location |
|----------|----------|
| Base | Remote org defaults (`.well-known/opencode`) |
| Global | `~/.config/opencode/opencode.json` |
| Env | `OPENCODE_CONFIG` env var path |
| Project | `./opencode.json` (highest standard) |
| Inline | `OPENCODE_CONFIG_CONTENT` env var |

---

## Codex CLI Setup

[Codex](https://github.com/openai/codex) is OpenAI's terminal-based AI coding agent with built-in MCP support. It uses **TOML** configuration at `~/.codex/config.toml`.

### Via CLI (Easiest)

```bash
codex mcp add calculator-demo -- mcp-anything serve /ABSOLUTE/PATH/TO/mcp-servers/calculator-demo
codex mcp add todo-demo -- mcp-anything serve /ABSOLUTE/PATH/TO/mcp-servers/todo-demo
codex mcp add weather-demo -- mcp-anything serve /ABSOLUTE/PATH/TO/mcp-servers/weather-demo
codex mcp add textutils-demo -- mcp-anything serve /ABSOLUTE/PATH/TO/mcp-servers/textutils-demo
```

### Via config.toml

Edit `~/.codex/config.toml` (global) or `.codex/config.toml` (project-scoped):

```toml
[mcp_servers.calculator-demo]
command = "mcp-anything"
args = ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/calculator-demo"]
enabled = true

[mcp_servers.todo-demo]
command = "mcp-anything"
args = ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/todo-demo"]
enabled = true

[mcp_servers.weather-demo]
command = "mcp-anything"
args = ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/weather-demo"]
enabled = true

[mcp_servers.textutils-demo]
command = "mcp-anything"
args = ["serve", "/ABSOLUTE/PATH/TO/mcp-servers/textutils-demo"]
enabled = true
```

### Server Options

| Key | Description |
|-----|-------------|
| `command` | Command to start the server (required) |
| `args` | Array of arguments |
| `env` | Map of static environment variables |
| `env_vars` | List of forwarded env var names |
| `enabled` | Enable on startup (`true`/`false`) |
| `enabled_tools` | Allow-list of tool names |
| `disabled_tools` | Deny-list of tool names |
| `default_tools_approval_mode` | `"auto"`, `"prompt"`, or `"approve"` |
| `startup_timeout_sec` | Seconds to wait for startup (default: 10) |
| `tool_timeout_sec` | Seconds to wait per tool call (default: 60) |

### Use the Demos in Codex

Just ask in the Codex TUI or `codex exec`:

```
Use the calculator to add 42 and 58
Add "Buy milk" to my todo list
What's the weather in Austin?
```

### Managing MCP Servers

```bash
codex mcp list                    # List configured servers
codex mcp add <name> -- <cmd>     # Add a new server
codex mcp update <name> -- <cmd>  # Update a server
codex mcp login <name>            # OAuth login (for remote servers)
```

---

## Workshop Flow

This project powers **Module 4** of the RGV AI Coalition *LLM Basics + MCP* workshop:

| Step | What You Do | What Happens |
|------|-------------|--------------|
| 1 | Open any demo script in your IDE | It's a normal Python CLI — nothing special |
| 2 | Run it directly | Works as expected |
| 3 | `mcp-anything generate ./demos/<name>` | Scans → designs → generates 5-10 MCP tools |
| 4 | Add the config to your MCP client | The LLM now has access to those tools |
| 5 | Ask the LLM to use them | Tool calls via MCP — **the aha moment** |

**Key insight:** You never modified the original scripts, wrote API boilerplate, or configured networking.

---

## Project Structure

```
rgvai-mcp-demo/
├── bin/
│   ├── mcp-demo.js           ← CLI runner (npx mcp-demo)
│   └── generate-all.js       ← Batch MCP server generator
├── demos/
│   ├── calculator/calculator.py
│   ├── todo/todo.py
│   ├── weather/weather.py
│   └── textutils/textutils.py
├── mcp-servers/              ← Auto-generated by mcp-anything
│   ├── calculator-demo/
│   ├── todo-demo/
│   ├── weather-demo/
│   └── textutils-demo/
├── examples/
│   ├── claude-desktop-config.json
│   ├── vscode-mcp-config.json
│   └── demo-interactions.md
├── package.json
└── README.md
```

---

## License

MIT — RGV AI Coalition

---

*Built with [`mcp-anything`](https://github.com/Type-MCP/mcp-anything) and [Model Context Protocol](https://modelcontextprotocol.io).*
