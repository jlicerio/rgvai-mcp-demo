#!/usr/bin/env python3
"""Text Utilities — CLI text processing tool for MCP demo."""

import argparse
import hashlib
import re
import sys


def count(text: str) -> dict:
    """Count characters, words, and lines in text."""
    lines = text.splitlines()
    words = text.split()
    return {
        "chars": len(text),
        "words": len(words),
        "lines": len(lines),
    }


def reverse(text: str) -> str:
    """Reverse the input string."""
    return text[::-1]


def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()


def lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    slug = slug.strip("-")
    return slug


def palindrome(text: str) -> dict:
    """Check if text (alphanumeric only, case-insensitive) is a palindrome."""
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    is_pal = cleaned == cleaned[::-1]
    return {
        "text": text,
        "is_palindrome": is_pal,
        "normalized": cleaned,
    }


def checksum(text: str) -> str:
    """Compute SHA-256 checksum of text."""
    return hashlib.sha256(text.encode()).hexdigest()


OPS = {
    "count": count,
    "reverse": reverse,
    "upper": uppercase,
    "lower": lowercase,
    "slugify": slugify,
    "palindrome": palindrome,
    "checksum": checksum,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Text Utilities CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # Commands that take TEXT argument
    for name in ("count", "reverse", "upper", "lower", "slugify", "checksum"):
        p = sub.add_parser(name, help=f"{name} text")
        p.add_argument("text", type=str, help="Text to process")

    # palindrome takes TEXT argument
    pal_p = sub.add_parser("palindrome", help="check if text is a palindrome")
    pal_p.add_argument("text", type=str, help="Text to check")

    args = parser.parse_args()

    if args.command == "palindrome":
        result = palindrome(args.text)
        print(f"  Text:     {result['text']}")
        print(f"  Normalized: {result['normalized']}")
        print(f"  Palindrome: {'✅ Yes' if result['is_palindrome'] else '❌ No'}")
        return

    op_func = OPS.get(args.command)
    if not op_func:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)

    result = op_func(args.text)

    if args.command == "count":
        print(f"  Characters: {result['chars']}")
        print(f"  Words:      {result['words']}")
        print(f"  Lines:      {result['lines']}")
    else:
        print(result)


if __name__ == "__main__":
    main()
