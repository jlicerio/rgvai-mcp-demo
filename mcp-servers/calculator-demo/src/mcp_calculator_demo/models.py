"""Data models for calculator-demo MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class RunCalculatorDemoParams:
    """Parameters for run_calculator_demo."""
    args: str

@dataclass
class ClearParams:
    """Parameters for clear."""
    args: str | None = None

@dataclass
class HistoryParams:
    """Parameters for history."""
    args: str | None = None

@dataclass
class SqrtParams:
    """Parameters for sqrt."""
    a: str

@dataclass
class RecordOperationParams:
    """Parameters for record_operation."""
    op: str
    a: str
    b: str
    result: str

@dataclass
class SaveHistoryParams:
    """Parameters for save_history."""
    entries: str

