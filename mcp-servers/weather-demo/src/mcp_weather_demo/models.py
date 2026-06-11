"""Data models for weather-demo MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class RunWeatherDemoParams:
    """Parameters for run_weather_demo."""
    args: str

@dataclass
class CompareParams:
    """Parameters for compare."""
    city1: str
    city2: str

@dataclass
class CurrentParams:
    """Parameters for current."""
    city: str

@dataclass
class ForecastParams:
    """Parameters for forecast."""
    city: str
    days: int | None = None

@dataclass
class CmdCompareParams:
    """Parameters for cmd_compare."""
    args: str

@dataclass
class CmdCurrentParams:
    """Parameters for cmd_current."""
    args: str

@dataclass
class CmdForecastParams:
    """Parameters for cmd_forecast."""
    args: str

