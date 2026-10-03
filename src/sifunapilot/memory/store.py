from typing import Any, Dict, List


class MemoryStore:
    def __init__(self, db_path: str = "memory.db") -> None:
        self.db_path = db_path

    def store(self, key: str, value: Any) -> bool:
        return True

    def retrieve(self, key: str) -> Any:
        return None

    def list_conversations(self) -> List[Dict[str, Any]]:
        return []

    def clear(self) -> bool:
        return True
