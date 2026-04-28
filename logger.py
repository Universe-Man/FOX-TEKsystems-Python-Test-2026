# ─────────────────────────────────────────
# Task 3 – OOP Design & API Thinking
# ─────────────────────────────────────────
from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, level: str, message: str) -> None:
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level.upper(),
            "message": message
        }
        self.logs.append(entry)

    def get_logs(self, level: str | None = None) -> list[dict]:
        if level is None:
            return self.logs
        return [entry for entry in self.logs if entry["level"] == level.upper()]

    def search(self, keyword: str) -> list[dict]:
        return [entry for entry in self.logs if keyword in entry["message"]]
