class ResumeAnalyzerError(Exception):
    """Base exception for the application."""


class ParseError(ResumeAnalyzerError):
    """Raised when resume parsing fails."""


class ValidationError(ResumeAnalyzerError):
    """Raised when extracted data is invalid."""
