from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol


@dataclass
class ModelRequest:
    messages: List[Dict[str, str]]
    model: str
    temperature: float = 0.7
    max_tokens: Optional[int] = None


@dataclass
class ModelResponse:
    content: str
    model: str
    usage: Optional[Dict[str, Any]] = None


class AIProvider(Protocol):
    async def generate(self, request: ModelRequest) -> ModelResponse:
        ...
