"""Data models for textutils-demo MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class RunTextutilsDemoParams:
    """Parameters for run_textutils_demo."""
    args: str

@dataclass
class PalindromeParams:
    """Parameters for palindrome."""
    text: str

@dataclass
class ChecksumParams:
    """Parameters for checksum."""
    text: str

@dataclass
class CountParams:
    """Parameters for count."""
    text: str

@dataclass
class LowercaseParams:
    """Parameters for lowercase."""
    text: str

@dataclass
class ReverseParams:
    """Parameters for reverse."""
    text: str

@dataclass
class SlugifyParams:
    """Parameters for slugify."""
    text: str

@dataclass
class UppercaseParams:
    """Parameters for uppercase."""
    text: str

