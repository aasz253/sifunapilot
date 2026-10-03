from typing import Optional

from sifunapilot.ai.base import AIProvider, ModelRequest, ModelResponse
from sifunapilot.ai.ollama import OllamaProvider
from sifunapilot.config.settings import get_settings


class ModelRouter:
    def __init__(self) -> None:
        self.settings = get_settings()
        self._provider: Optional[AIProvider] = None

    def get_provider(self) -> AIProvider:
        provider_name = self.settings.ai.provider.lower()
        if provider_name == "ollama":
            return OllamaProvider(
                host=self.settings.ai.host or "http://localhost:11434",
                model=self.settings.ai.model,
            )
        # Default to ollama
        return OllamaProvider(model=self.settings.ai.model)

    async def generate(self, request: ModelRequest) -> ModelResponse:
        provider = self.get_provider()
        return await provider.generate(request)
