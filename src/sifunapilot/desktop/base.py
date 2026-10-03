from typing import Any, Protocol


class DesktopAdapter(Protocol):
    def open_application(self, app_name: str, **kwargs: Any) -> str:
        ...

    def close_application(self, app_name: str, **kwargs: Any) -> str:
        ...

    def focus_window(self, window_title: str, **kwargs: Any) -> str:
        ...

    def screenshot(self, **kwargs: Any) -> str:
        ...

    def key_press(self, keys: str, **kwargs: Any) -> str:
        ...

    def type_text(self, text: str, **kwargs: Any) -> str:
        ...

    def click(self, x: int = 0, y: int = 0, **kwargs: Any) -> str:
        ...

    def move_mouse(self, x: int, y: int, **kwargs: Any) -> str:
        ...
