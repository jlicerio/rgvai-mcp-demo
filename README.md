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

## Raspberry Pi Setup

This demo runs great on a Raspberry Pi (3B+ or newer, Raspberry Pi OS). A Pi makes an excellent **dedicated MCP server station** — always on, low power, serving tools to your main machine over the network.

### Install on a Pi

```bash
# Install Python 3.10+ (Pi OS Lite works)
sudo apt update && sudo apt install -y python3 python3-pip

# Install mcp-anything
pip3 install mcp-anything

# Clone the demo
git clone https://github.com/jlicerio/rgvai-mcp-demo.git
cd rgvai-mcp-demo

# Generate MCP servers (this runs fine on a Pi)
python3 -m pip install mcp uvicorn
node bin/generate-all.js
```

### Run the MCP Servers on a Pi (Remote Setup)

For the workshop, one Pi can serve MCP tools to every student's laptop:

```bash
# On the Pi — start the demo servers with HTTP transport
# Each gets a unique port
cd ~/rgvai-mcp-demo

mcp-anything serve ./mcp-servers/calculator-demo --port 8101 &
mcp-anything serve ./mcp-servers/todo-demo --port 8102 &
mcp-anything serve ./mcp-servers/weather-demo --port 8103 &
mcp-anything serve ./mcp-servers/textutils-demo --port 8104 &
```

### Connect to a Remote Pi from Your Laptop

Students configure their MCP client to point to the Pi's IP address and HTTP port. This works with any MCP client that supports URL-based server config:

```json
{
  "mcpServers": {
    "calculator-demo": {
      "url": "http://192.168.1.PI_IP:8101/mcp"
    },
    "todo-demo": {
      "url": "http://192.168.1.PI_IP:8102/mcp"
    },
    "weather-demo": {
      "url": "http://192.168.1.PI_IP:8103/mcp"
    },
    "textutils-demo": {
      "url": "http://192.168.1.PI_IP:8104/mcp"
    }
  }
}
```

> **Tip:** Use a `.local` hostname (`raspberrypi.local`) or Tailscale IP so you don't need static IPs.

### Auto-Start on Boot (Pi as Appliance)

```bash
# Create a systemd service
sudo tee /etc/systemd/system/mcp-demo.service << 'EOF'
[Unit]
Description=RGV AI MCP Demo Suite
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/rgvai-mcp-demo
ExecStart=/usr/bin/python3 -m mcp_anything serve ./mcp-servers/calculator-demo --port 8101
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable mcp-demo
sudo systemctl start mcp-demo
```

### Why Use a Pi?

| Reason | Detail |
|--------|--------|
| **Portable** | Take the whole demo in your pocket — great for workshops |
| **Low power** | Runs 24/7 on 5W — always-on MCP server |
| **Network shared** | One Pi serves tools to everyone on the same LAN |
| **ARM-native** | MCP, Python, mcp-anything all work on ARM64 |
| **No install on laptops** | Students just add a URL to their client config — nothing to install |

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
