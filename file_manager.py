import json
from pathlib import Path

from exceptions import ResumeAnalyzerError


def read_text_file(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise ResumeAnalyzerError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")


def read_json_file(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise ResumeAnalyzerError(f"File not found: {file_path}")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_text_file(file_path: str, content: str) -> None:
    """
    Write text to a file.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(content, encoding="utf-8")


def write_json_file(file_path: str, data: dict) -> None:
    """
    Save dictionary as JSON.
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)