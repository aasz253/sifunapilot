from typing import Any

from sifunapilot.desktop.base import DesktopAdapter


class LinuxDesktop(DesktopAdapter):
    def open_application(self, app_name: str, **kwargs: Any) -> str:
        return f"✓ Launched {app_name} (Linux)"

    def close_application(self, app_name: str, **kwargs: Any) -> str:
        return f"✓ Closed {app_name} (Linux)"

    def focus_window(self, window_title: str, **kwargs: Any) -> str:
        return f"✓ Focused {window_title}"

    def screenshot(self, **kwargs: Any) -> str:
        return "✓ Screenshot taken"

    def key_press(self, keys: str, **kwargs: Any) -> str:
        return f"✓ Pressed {keys}"

    def type_text(self, text: str, **kwargs: Any) -> str:
        return f"✓ Typed text"

    def click(self, x: int = 0, y: int = 0, **kwargs: Any) -> str:
        return f"✓ Clicked at ({x}, {y})"

    def move_mouse(self, x: int, y: int, **kwargs: Any) -> str:
        return f"✓ Moved mouse to ({x}, {y})"
