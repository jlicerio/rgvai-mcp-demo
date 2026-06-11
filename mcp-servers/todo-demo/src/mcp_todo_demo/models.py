"""Data models for todo-demo MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class RunTodoDemoParams:
    """Parameters for run_todo_demo."""
    args: str

@dataclass
class AddParams:
    """Parameters for add."""
    text: str

@dataclass
class ClearParams:
    """Parameters for clear."""
    args: str | None = None

@dataclass
class DeleteParams:
    """Parameters for delete."""
    id: int

@dataclass
class DoneParams:
    """Parameters for done."""
    id: int

@dataclass
class ListParams:
    """Parameters for list."""
    args: str | None = None

@dataclass
class CmdAddParams:
    """Parameters for cmd_add."""
    args: str

@dataclass
class CmdClearParams:
    """Parameters for cmd_clear."""
    args: str

@dataclass
class CmdListParams:
    """Parameters for cmd_list."""
    args: str

@dataclass
class SaveTasksParams:
    """Parameters for save_tasks."""
    tasks: str

