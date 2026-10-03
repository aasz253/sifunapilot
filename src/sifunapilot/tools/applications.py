from typing import Any


class ApplicationTools:
    async def open_app(self, app_name: str, **kwargs: Any) -> str:
        return f"✓ Opened application: {app_name}"

    async def close_app(self, app_name: str, **kwargs: Any) -> str:
        return f"✓ Closed application: {app_name}"

    async def list_apps(self, **kwargs: Any) -> str:
        return "✓ Available apps: Chrome, Firefox, VS Code, Terminal, Files"
