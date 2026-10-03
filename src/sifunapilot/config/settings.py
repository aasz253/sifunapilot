from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AgentSettings(BaseSettings):
    mode: str = Field(default="assist")  # assist, agent, safe
    max_steps: int = Field(default=30)
    retry_limit: int = Field(default=2)
    require_confirmation: bool = Field(default=True)


class AISettings(BaseSettings):
    provider: str = Field(default="ollama")
    model: str = Field(default="llama3.2:3b")  # 8GB RAM friendly
    host: Optional[str] = None
    api_key: Optional[str] = None


class VoiceSettings(BaseSettings):
    enabled: bool = Field(default=False)


class BrowserSettings(BaseSettings):
    browser: str = Field(default="chromium")  # chromium, firefox, webkit
    headless: bool = Field(default=False)
    profile_dir: Optional[str] = None


class SecuritySettings(BaseSettings):
    require_confirmation: bool = Field(default=True)


class LoggingSettings(BaseSettings):
    level: str = Field(default="INFO")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="SIFUNAPILOT_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    agent: AgentSettings = Field(default_factory=AgentSettings)
    ai: AISettings = Field(default_factory=AISettings)
    voice: VoiceSettings = Field(default_factory=VoiceSettings)
    browser: BrowserSettings = Field(default_factory=BrowserSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    logging: LoggingSettings = Field(default_factory=LoggingSettings)

    @property
    def config_dir(self) -> Path:
        return Path.home() / ".config" / "sifunapilot"

    @property
    def data_dir(self) -> Path:
        return Path.home() / ".sifunapilot"

    def ensure_dirs(self) -> None:
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "browser").mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    return Settings()
