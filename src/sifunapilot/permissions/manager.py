from sifunapilot.permissions.policy import get_policy, PermissionLevel


class PermissionManager:
    def __init__(self) -> None:
        self.policy = get_policy()

    def check_permission(self, action: str) -> PermissionLevel:
        # Simple mapping
        mapping = {
            "browser_navigation": self.policy.browser_navigation,
            "browser_click": self.policy.browser_click,
            "browser_type": self.policy.browser_type,
            "browser_upload": self.policy.browser_upload,
            "file_read": self.policy.file_read,
            "file_write": self.policy.file_write,
            "file_delete": self.policy.file_delete,
            "terminal": self.policy.terminal,
            "app_launch": self.policy.app_launch,
        }
        return mapping.get(action, PermissionLevel.SAFE)

    def requires_confirmation(self, action: str) -> bool:
        level = self.check_permission(action)
        return level in (PermissionLevel.CONFIRM, PermissionLevel.RESTRICTED)
