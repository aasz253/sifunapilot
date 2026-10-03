from typing import Protocol


class STTProvider(Protocol):
    def transcribe(self, audio_path: str) -> str:
        ...


class TTSProvider(Protocol):
    def synthesize(self, text: str, output_path: str) -> str:
        ...


class WakeWordDetector(Protocol):
    def detect(self) -> bool:
        ...
