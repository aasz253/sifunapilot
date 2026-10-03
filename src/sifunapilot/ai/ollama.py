from typing import Dict, List, Optional

from sifunapilot.ai.base import AIProvider, ModelRequest, ModelResponse


class OllamaProvider(AIProvider):
    def __init__(self, host: str = "http://localhost:11434", model: str = "llama3.1"):
        self.host = host
        # Default to a lightweight model suitable for 8GB RAM
        self.model = model or "llama3.2:3b"

    async def generate(self, request: ModelRequest) -> ModelResponse:
        # Stub implementation - will be enhanced later
        return ModelResponse(
            content="Action planned (stub implementation)",
            model=request.model or self.model,
            usage={"prompt_tokens": 0, "completion_tokens": 0},
        )
