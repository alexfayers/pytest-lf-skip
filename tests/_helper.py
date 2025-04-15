from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


def replace_file_text(path: Path, old: str, new: str) -> None:
    with path.open("r") as f:
        text = f.read()

    text = text.replace(old, new)

    with path.open("w") as f:
        f.write(text)
