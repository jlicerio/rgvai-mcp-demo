#!/usr/bin/env python3
"""CLI calculator with JSON history tracking."""

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

HISTORY_FILE = Path(__file__).resolve().parent / ".calc_history.json"


def load_history():
    if HISTORY_FILE.exists():
        try:
            return json.loads(HISTORY_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_history(entries):
    HISTORY_FILE.write_text(json.dumps(entries, indent=2))


def record_operation(op, a, b, result):
    history = load_history()
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operation": op,
        "operands": [a] if b is None else [a, b],
        "result": result,
    }
    history.append(entry)
    save_history(history)


def handle_args(args):
    b = None
    a = None
    try:
        if hasattr(args, "a") and args.a is not None:
            a = float(args.a)
        if hasattr(args, "b") and args.b is not None:
            b = float(args.b)
    except ValueError as e:
        print(f"Error: invalid number - {e}", file=sys.stderr)
        sys.exit(1)

    if args.command == "add":
        if a is None or b is None:
            print("Error: add requires two arguments", file=sys.stderr)
            sys.exit(1)
        result = a + b
        print(result)
        record_operation("add", a, b, result)

    elif args.command == "subtract":
        if b is None:
            print("Error: subtract requires two arguments", file=sys.stderr)
            sys.exit(1)
        result = a - b
        print(result)
        record_operation("subtract", a, b, result)

    elif args.command == "multiply":
        if b is None:
            print("Error: multiply requires two arguments", file=sys.stderr)
            sys.exit(1)
        result = a * b
        print(result)
        record_operation("multiply", a, b, result)

    elif args.command == "divide":
        if b is None:
            print("Error: divide requires two arguments", file=sys.stderr)
            sys.exit(1)
        if b == 0:
            print("Error: division by zero", file=sys.stderr)
            sys.exit(1)
        result = a / b
        print(result)
        record_operation("divide", a, b, result)

    elif args.command == "power":
        if b is None:
            print("Error: power requires two arguments", file=sys.stderr)
            sys.exit(1)
        result = a ** b
        print(result)
        record_operation("power", a, b, result)

    elif args.command == "sqrt":
        if a < 0:
            print("Error: cannot take sqrt of a negative number", file=sys.stderr)
            sys.exit(1)
        result = math.sqrt(a)
        print(result)
        record_operation("sqrt", a, None, result)

    elif args.command == "history":
        history = load_history()
        if not history:
            print("No history yet.")
            return
        for entry in history:
            op = entry["operation"]
            operands = entry["operands"]
            res = entry["result"]
            ts = entry["timestamp"]
            if op == "sqrt":
                print(f"  [{ts}] sqrt({operands[0]}) = {res}")
            else:
                print(f"  [{ts}] {operands[0]} {op} {operands[1]} = {res}")

    elif args.command == "clear":
        save_history([])
        print("History cleared.")


def build_parser():
    parser = argparse.ArgumentParser(description="CLI calculator")
    sub = parser.add_subparsers(dest="command", title="operations")

    for name, help_text in [
        ("add", "Add two numbers"),
        ("subtract", "Subtract two numbers"),
        ("multiply", "Multiply two numbers"),
        ("divide", "Divide two numbers"),
        ("power", "Raise a to power of b"),
    ]:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("a", type=str, help="First number")
        p.add_argument("b", type=str, help="Second number")

    sqrt_p = sub.add_parser("sqrt", help="Square root")
    sqrt_p.add_argument("a", type=str, help="Number")

    sub.add_parser("history", help="Show calculation history")
    sub.add_parser("clear", help="Clear calculation history")

    return parser


def main():
    parser = build_parser()
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    handle_args(args)


if __name__ == "__main__":
    main()
