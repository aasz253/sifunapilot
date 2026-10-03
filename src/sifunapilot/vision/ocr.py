from typing import Optional


class OCR:
    def __init__(self) -> None:
        self.enabled = False

    def extract(self, image_path: str) -> str:
        return f"✓ OCR would extract from {image_path}"
