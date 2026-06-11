#!/usr/bin/env node

/**
 * generate-all.js — Generate MCP servers for all demo apps using mcp-anything.
 *
 * Usage: node bin/generate-all.js
 *
 * Requires: mcp-anything installed (pip install mcp-anything)
 */

import { execSync } from "child_process";
import { existsSync, mkdirSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..");
const SERVERS_DIR = resolve(ROOT, "mcp-servers");
const DEMOS_DIR = resolve(ROOT, "demos");

const DEMOS = [
  { name: "calculator-demo", dir: "calculator", file: "calculator.py", emoji: "🧮" },
  { name: "todo-demo", dir: "todo", file: "todo.py", emoji: "✅" },
  { name: "weather-demo", dir: "weather", file: "weather.py", emoji: "🌤" },
  { name: "textutils-demo", dir: "textutils", file: "textutils.py", emoji: "📝" },
];

if (!existsSync(SERVERS_DIR)) {
  mkdirSync(SERVERS_DIR, { recursive: true });
}

// Verify mcp-anything
try {
  execSync("which mcp-anything", { encoding: "utf-8", stdio: "pipe" });
} catch {
  console.error("❌ mcp-anything not found. Install: pip install mcp-anything");
  process.exit(1);
}

console.log("╔══════════════════════════════════════════╗");
console.log("║  Generating MCP Servers for All Demos   ║");
console.log("╚══════════════════════════════════════════╝\n");

let allOk = true;

for (const demo of DEMOS) {
  const sourceDir = resolve(DEMOS_DIR, demo.dir);
  const sourceFile = resolve(sourceDir, demo.file);
  const outDir = resolve(SERVERS_DIR, demo.name);

  if (!existsSync(sourceDir)) {
    console.log(`  ${demo.emoji}  ${demo.name} — directory not found: ${sourceDir}`);
    allOk = false;
    continue;
  }

  console.log(`  ${demo.emoji}  ${demo.name}...`);

  try {
    execSync(
      `mcp-anything generate "${sourceDir}" --name "${demo.name}" --transport stdio -o "${outDir}"`,
      { cwd: ROOT, encoding: "utf-8", stdio: "inherit", timeout: 180 }
    );
    console.log(`     ✅ ${outDir}\n`);
  } catch (e) {
    console.log(`     ❌ ${e.message}\n`);
    allOk = false;
  }
}

if (allOk) {
  console.log("\n✅ All MCP servers generated!");
  console.log("\n📋 Add this to your MCP client config:");
  console.log(`{\n  "mcpServers": {`);
  for (const demo of DEMOS) {
    const outDir = resolve(SERVERS_DIR, demo.name);
    console.log(`    "${demo.name}": { "command": "mcp-anything", "args": ["serve", "${outDir}"] },`);
  }
  console.log(`  }\n}`);
} else {
  console.log("\n⚠️  Some servers failed to generate. See errors above.");
  process.exit(1);
}
