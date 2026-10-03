from typing import Any, Callable, Dict, List, Optional, Protocol


class ToolSchema(Protocol):
    name: str
    description: str
    permission: str


class Tool:
    def __init__(
        self,
        name: str,
        description: str,
        permission: str = "safe",
        executor: Optional[Callable[..., Any]] = None,
    ):
        self.name = name
        self.description = description
        self.permission = permission
        self.executor = executor

    async def execute(self, **kwargs: Any) -> Any:
        if self.executor:
            return await self.executor(**kwargs)
        return None


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def list_all(self) -> List[Tool]:
        return list(self._tools.values())

    def list_by_permission(self, permission: str) -> List[Tool]:
        return [t for t in self._tools.values() if t.permission == permission]
