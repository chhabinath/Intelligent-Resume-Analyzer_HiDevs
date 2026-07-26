from pathlib import Path

from exceptions import ResumeAnalyzerError


def read_text_file(file_path: str) -> str:
    """
    Read and return the contents of a text file.
    """
    path = Path(file_path)

    if not path.exists():
        raise ResumeAnalyzerError(f"File not found: {file_path}")

    return path.read_text(encoding="utf-8")