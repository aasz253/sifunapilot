from typing import Any, Optional

from sifunapilot.browser.browser import PlaywrightBrowser


class BrowserTools:
    def __init__(self) -> None:
        self._browser: Optional[PlaywrightBrowser] = None

    def _get_browser(self) -> PlaywrightBrowser:
        if self._browser is None:
            self._browser = PlaywrightBrowser()
        return self._browser

    async def open_browser(self, browser: str = "chromium", **kwargs: Any) -> str:
        return await self._get_browser().launch(browser_type=browser, **kwargs)

    async def close_browser(self, **kwargs: Any) -> str:
        result = await self._get_browser().close()
        self._browser = None
        return result

    async def open_url(self, url: str, **kwargs: Any) -> str:
        return await self._get_browser().navigate(url)

    async def navigate(self, url: str = "google.com", **kwargs: Any) -> str:
        return await self._get_browser().navigate(url)

    async def type_text(self, text: str, selector: str = "", **kwargs: Any) -> str:
        return await self._get_browser().type_text(text, selector if selector else None)

    async def press_enter(self, **kwargs: Any) -> str:
        return await self._get_browser().press_enter()

    async def click(self, selector: str = "", **kwargs: Any) -> str:
        return await self._get_browser().click(selector) if selector else "✓ Clicked"

    async def new_tab(self, **kwargs: Any) -> str:
        return await self._get_browser().new_tab()

    async def close_tab(self, **kwargs: Any) -> str:
        return await self._get_browser().close_tab()

    async def screenshot(self, **kwargs: Any) -> str:
        return await self._get_browser().screenshot(**kwargs)
