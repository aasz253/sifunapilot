from typing import Any, Dict


class Observer:
    def __init__(self) -> None:
        pass

    def observe(self, result: Dict[str, Any]) -> Dict[str, Any]:
        return {"observed": True, **result}
