from typing import Optional


class STTEngine:
    def __init__(self) -> None:
        self.enabled = False

    def listen(self, timeout: int = 5) -> str:
        if not self.enabled:
            return ""
        return ""


def get_stt() -> STTEngine:
    return STTEngine()
