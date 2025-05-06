# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Simple script to validate strings using the conventional commit format.

Used in CI to ensure that PR titles are consistent, allowing for contributions to use any commit style
they want while still allowing us to generate a changelog.
"""

from __future__ import annotations

import argparse
import re
import sys

# The types of changes that are allowed in a message.
ALLOWED_TYPES = ["feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"]

# Make sure the message has a scope, e.g. "fix(scope): message"
FORMAT_REGEX = re.compile(r"^([\w ]+)\((\w+)\)\!?: .+")


def validate_commit_message(message: str) -> bool:
    """Validate a commit message against the conventional commit format.

    Args:
        message (str): The commit message to validate.

    Returns:
        bool: True if the message is valid, False otherwise.
    """
    # Check if the message matches the format
    match = FORMAT_REGEX.match(message)
    if not match:
        # If the message doesn't match the format, it is invalid
        print(f"Invalid message format: {message}")
        print("Expected format: <type>(<scope>): <description>")
        return False

    # Check if the type is allowed
    commit_type = match.group(1)
    if commit_type not in ALLOWED_TYPES:
        print(f"Invalid commit type: {commit_type}")
        print(f"Allowed types: {', '.join(ALLOWED_TYPES)}")
        return False

    # Check if the scope is lowercase
    scope = match.group(2)
    if not scope.islower():
        print(f"Invalid scope: {scope}")
        print("Scope must be lowercase.")
        return False

    # If the message is valid, return True
    return True


def parse_args() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Validate commit messages.")
    parser.add_argument("message", type=str, help="The commit message to validate.")
    return parser.parse_args()


def main() -> None:
    """Main function to validate commit messages."""
    args = parse_args()
    message = args.message

    if not validate_commit_message(message):
        sys.exit(1)


if __name__ == "__main__":
    main()
