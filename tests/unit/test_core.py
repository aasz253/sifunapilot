from sifunapilot.permissions.policy import get_policy, PermissionLevel
from sifunapilot.config.settings import get_settings
from sifunapilot.tools.registry import ToolRegistry, Tool


def test_permission_policy_defaults():
    policy = get_policy()
    assert policy.browser_navigation == PermissionLevel.SAFE
    assert policy.sudo == PermissionLevel.BLOCKED


def test_settings_defaults():
    settings = get_settings()
    assert settings.ai.provider == "ollama"
    assert settings.agent.mode == "assist"


def test_tool_registry():
    registry = ToolRegistry()
    tool = Tool(name="test.tool", description="Test tool", permission="safe")
    registry.register(tool)
    assert registry.get("test.tool") is not None
    assert len(registry.list_all()) == 1
