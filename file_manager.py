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