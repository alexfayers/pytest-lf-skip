from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


@dataclass
class Outcome:
    passed: int = 0
    skipped: int = 0
    failed: int = 0
    deselected: int = 0


@dataclass
class LineSearch:
    search: str
    count: int = 1


@dataclass
class FileReplace:
    old: str
    new: str


@dataclass
class ExpectedResult:
    outcome: Outcome
    test_file_replace: FileReplace | None = None
    line_searches: Iterable[LineSearch] | None = None
    prepend_args: Iterable[str] | None = None
