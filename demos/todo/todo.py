#!/usr/bin/env python3
"""CLI todo list manager with JSON file persistence."""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / ".todos.json"


def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def cmd_add(args):
    tasks = load_tasks()
    task_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({
        "id": task_id,
        "text": args.text,
        "done": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })
    save_tasks(tasks)
    print(f"Added task #{task_id}: {args.text}")


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"  [{status}] #{t['id']} {t['text']}")


def cmd_done(args):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == args.id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task #{args.id} marked as done.")
            return
    print(f"Error: task #{args.id} not found", file=sys.stderr)
    sys.exit(1)


def cmd_delete(args):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != args.id]
    if len(new_tasks) == len(tasks):
        print(f"Error: task #{args.id} not found", file=sys.stderr)
        sys.exit(1)
    save_tasks(new_tasks)
    print(f"Deleted task #{args.id}.")


def cmd_clear(args):
    save_tasks([])
    print("All tasks cleared.")


def main():
    parser = argparse.ArgumentParser(description="Todo List Manager")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a task")
    p_add.add_argument("text", type=str, help="Task description")

    sub.add_parser("list", help="List all tasks")

    p_done = sub.add_parser("done", help="Mark a task as done")
    p_done.add_argument("id", type=int, help="Task ID")

    p_del = sub.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int, help="Task ID")

    sub.add_parser("clear", help="Delete all tasks")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Dispatch (Python 3.9 compatible - no match/case)
    if args.command == "add":
        cmd_add(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "done":
        cmd_done(args)
    elif args.command == "delete":
        cmd_delete(args)
    elif args.command == "clear":
        cmd_clear(args)


if __name__ == "__main__":
    main()
