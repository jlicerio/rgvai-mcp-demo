#!/usr/bin/env node

/**
 * mcp-demo — CLI runner for the RGV AI MCP Demo Suite.
 *
 * Usage:
 *   npx mcp-demo              # interactive menu
 *   npx mcp-demo list         # list available demos
 *   npx mcp-demo run <demo>   # run a specific demo
 *   npx mcp-demo generate     # generate MCP servers for all demos
 *   npx mcp-demo help         # show this help
 */

import { execSync } from "child_process";
import { existsSync, readFileSync } from "fs";
import { createInterface } from "readline";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..");

const DEMOS = {
  calculator: {
    file: "demos/calculator/calculator.py",
    description: "Calculator — add, subtract, multiply, divide, power, sqrt",
    emoji: "🧮",
  },
  todo: {
    file: "demos/todo/todo.py",
    description: "Todo List — add, list, done, delete, clear tasks",
    emoji: "✅",
  },
  weather: {
    file: "demos/weather/weather.py",
    description: "Weather — simulated current/forecast/compare for any city",
    emoji: "🌤",
  },
  textutils: {
    file: "demos/textutils/textutils.py",
    description: "Text Utils — count, reverse, case, slugify, palindrome, checksum",
    emoji: "📝",
  },
};

function python(...args) {
  const cmd = `python3 ${args.join(" ")}`;
  try {
    const out = execSync(cmd, { cwd: ROOT, encoding: "utf-8", stdio: ["pipe", "pipe", "pipe"] });
    return { ok: true, output: out.trim() };
  } catch (e) {
    return { ok: false, output: e.stderr?.trim() || e.message };
  }
}

function banner(text) {
  console.log(`\n\x1b[1m╔══════════════════════════════════════════════════╗\x1b[0m`);
  console.log(`\x1b[1m║  ${text.padEnd(45)}\x1b[0m║`);
  console.log(`\x1b[1m╚══════════════════════════════════════════════════╝\x1b[0m\n`);
}

function showHelp() {
  console.log(`
  \x1b[1mRGV AI — MCP Demo Suite\x1b[0m

  \x1b[2mUsage:\x1b[0m
    npx mcp-demo              Open interactive demo menu
    npx mcp-demo list         List available demos
    npx mcp-demo run <demo>   Run a specific demo (calculator|todo|weather|textutils)
    npx mcp-demo generate     Generate MCP servers for all demos
    npx mcp-demo help         Show this help

  \x1b[2mExamples:\x1b[0m
    npx mcp-demo run calculator add 5 3
    npx mcp-demo run todo add "Buy milk"
    npx mcp-demo run weather current Austin
    npx mcp-demo run textutils reverse "hello"

  \x1b[2mMCP Integration:\x1b[0m
    After running \x1b[3mnpx mcp-demo generate\x1b[0m, add this to your MCP client config:

    {
      "mcpServers": {
        "calculator-demo": {
          "command": "mcp-anything",
          "args": ["serve", "${ROOT}/mcp-servers/calculator-demo"]
        },
        "todo-demo": {
          "command": "mcp-anything",
          "args": ["serve", "${ROOT}/mcp-servers/todo-demo"]
        },
        "weather-demo": {
          "command": "mcp-anything",
          "args": ["serve", "${ROOT}/mcp-servers/weather-demo"]
        },
        "textutils-demo": {
          "command": "mcp-anything",
          "args": ["serve", "${ROOT}/mcp-servers/textutils-demo"]
        }
      }
    }
  `);
}

function listDemos() {
  banner("Available Demos");
  for (const [name, demo] of Object.entries(DEMOS)) {
    const mcpDir = resolve(ROOT, "mcp-servers", `${name}-demo`);
    const hasMcp = existsSync(mcpDir);
    console.log(`  ${demo.emoji}  \x1b[1m${name}\x1b[0m`);
    console.log(`     ${demo.description}`);
    console.log(`     ${hasMcp ? "✅ MCP server generated" : "  ⚡ Run 'npx mcp-demo generate' to enable MCP"}`);
    console.log();
  }
}

function runDemo(args) {
  if (args.length < 1) {
    console.log("Usage: npx mcp-demo run <demo> [args...]");
    console.log("Demos: " + Object.keys(DEMOS).join(", "));
    process.exit(1);
  }

  const name = args[0];
  const demoArgs = args.slice(1);

  if (!DEMOS[name]) {
    console.log(`Unknown demo "${name}". Available: ${Object.keys(DEMOS).join(", ")}`);
    process.exit(1);
  }

  const demo = DEMOS[name];
  const script = resolve(ROOT, demo.file);

  if (!existsSync(script)) {
    console.log(`Script not found: ${script}`);
    process.exit(1);
  }

  banner(`${demo.emoji}  ${name} ${demoArgs.join(" ") || "(help)"}`);

  const fullArgs = [script, ...(demoArgs.length ? demoArgs : ["--help"])];
  const result = python(...fullArgs);
  console.log(result.output);
  process.exit(result.ok ? 0 : 1);
}

function generateServers() {
  banner("Generating MCP Servers");

  // Check if mcp-anything is available
  try {
    execSync("which mcp-anything", { encoding: "utf-8" });
  } catch {
    console.log("  ❌ mcp-anything not found. Install it first:");
    console.log("     pip install mcp-anything");
    process.exit(1);
  }

  const serversDir = resolve(ROOT, "mcp-servers");

  for (const [name, demo] of Object.entries(DEMOS)) {
    const outDir = resolve(serversDir, `${name}-demo`);
    console.log(`\n  ${demo.emoji}  Generating \x1b[1m${name}-demo\x1b[0m...`);

    const demosDir = resolve(ROOT, "demos");
    const specificFile = resolve(demosDir, `${name}.py`);

    try {
      execSync(
        `mcp-anything generate "${specificFile}" --name "${name}-demo" --transport stdio -o "${outDir}"`,
        { cwd: ROOT, encoding: "utf-8", stdio: "inherit", timeout: 120 }
      );
      console.log(`     ✅ Generated to ${outDir}`);
    } catch (e) {
      console.log(`     ❌ Failed: ${e.message}`);
    }
  }

  console.log("\n  ✅ Done! Add the config above to your MCP client.");
}

function interactiveMenu() {
  banner("RGV AI MCP Demo Suite");

  const names = Object.keys(DEMOS);
  console.log("  Select a demo to run:\n");
  names.forEach((name, i) => {
    const demo = DEMOS[name];
    console.log(`  \x1b[1m${i + 1}\x1b[0m) ${demo.emoji} ${name} — ${demo.description}`);
  });
  console.log(`  \x1b[1mg\x1b[0m) Generate MCP servers for all demos`);
  console.log(`  \x1b[1ml\x1b[0m) List available demos`);
  console.log(`  \x1b[1mq\x1b[0m) Quit\n`);

  const rl = createInterface({ input: process.stdin, output: process.stdout });
  rl.question("  Choice: ", (answer) => {
    rl.close();
    const idx = parseInt(answer) - 1;
    if (idx >= 0 && idx < names.length) {
      runDemo([names[idx]]);
    } else if (answer === "g") {
      generateServers();
    } else if (answer === "l") {
      listDemos();
    } else if (answer === "q") {
      process.exit(0);
    } else {
      console.log("Invalid choice.");
      process.exit(1);
    }
  });
}

// --- Main ---
const cmd = process.argv[2];

switch (cmd) {
  case "help":
  case "--help":
  case "-h":
    showHelp();
    break;
  case "list":
  case "ls":
    listDemos();
    break;
  case "run":
    runDemo(process.argv.slice(3));
    break;
  case "generate":
    generateServers();
    break;
  default:
    interactiveMenu();
    break;
}
