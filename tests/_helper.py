from pathlib import Path


def replace_file_text(path: Path, old: str, new: str):
    with path.open("r") as f:
        text = f.read()

    text = text.replace(old, new)

    with path.open("w") as f:
        f.write(text)
