class ResumeAnalyzerError(Exception):
    """Base exception for the application."""
    pass


class ParseError(ResumeAnalyzerError):
    """Raised when resume parsing fails."""
    pass


class ValidationError(ResumeAnalyzerError):
    """Raised when extracted data is invalid."""
    pass