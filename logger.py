# ─────────────────────────────────────────
# Task 3 – OOP Design & API Thinking
# ─────────────────────────────────────────
from datetime import datetime

class Logger:
    def __init__(self):
        # Initialize storage for log entries
        pass

    def log(self, level: str, message: str) -> None:
        """Record a log entry with a timestamp, level, and message."""
        # Create and store a log entry
        pass

    def get_logs(self, level: str | None = None) -> list[dict]:
        """
        Return all stored log entries.
        If level is provided, return only entries matching that level.
        """
        pass

    def search(self, keyword: str) -> list[dict]:
        """Return all log entries whose message contains the keyword."""
        pass
