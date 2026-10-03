from typing import Any, Dict


class Recovery:
    def __init__(self) -> None:
        self.retry_limit = 2

    def recover(self, error: str, attempt: int) -> Dict[str, Any]:
        if attempt < self.retry_limit:
            return {"action": "retry", "attempt": attempt + 1}
        return {"action": "stop", "reason": "retry limit exceeded"}
