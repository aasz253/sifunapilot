from typing import Any, Optional

from playwright.async_api import async_playwright, Browser, BrowserContext, Page


class PlaywrightBrowser:
    def __init__(self) -> None:
        self._playwright = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None

    async def launch(self, browser_type: str = "chromium", headless: bool = False, profile_dir: Optional[str] = None) -> str:
        try:
            self._playwright = await async_playwright().start()
            bt = browser_type.lower()
            if bt in ("chrome", "google chrome", "chromium", "msedge", "edge", "microsoft edge"):
                browser_launcher = self._playwright.chromium
                if bt in ("msedge", "edge", "microsoft edge"):
                    browser_launcher = self._playwright.chromium  # fallback; real edge needs channel
                    launch_options: dict[str, Any] = {"headless": headless, "channel": "msedge"}
                else:
                    launch_options = {"headless": headless}
            elif bt in ("firefox", "mozilla firefox"):
                browser_launcher = self._playwright.firefox
                launch_options = {"headless": headless}
            elif bt in ("webkit", "safari"):
                browser_launcher = self._playwright.webkit
                launch_options = {"headless": headless}
            elif bt in ("brave",):
                browser_launcher = self._playwright.chromium
                launch_options = {"headless": headless, "channel": "chrome"}
            else:
                browser_launcher = self._playwright.chromium
                launch_options = {"headless": headless}

            if profile_dir:
                launch_options["user_data_dir"] = profile_dir
            self._browser = await browser_launcher.launch(**launch_options)
            self._context = await self._browser.new_context()
            self._page = await self._context.new_page()
            return f"✓ Launched {bt} browser"
        except Exception as e:
            return f"✗ Failed to launch browser: {e}"

    async def close(self) -> str:
        try:
            if self._page:
                await self._page.close()
            if self._context:
                await self._context.close()
            if self._browser:
                await self._browser.close()
            if self._playwright:
                await self._playwright.stop()
            self._page = None
            return "✓ Browser closed"
        except Exception as e:
            return f"✗ Failed to close browser: {e}"

    async def navigate(self, url: str) -> str:
        try:
            if not self._page:
                return "✗ No active page"
            if not url.startswith(("http://", "https://")):
                url = f"https://{url}"
            await self._page.goto(url)
            return f"✓ Navigated to {url}"
        except Exception as e:
            return f"✗ Navigation failed: {e}"

    async def type_text(self, text: str, selector: str = "input[name='q'], input[type='search'], input[type='text'], textarea") -> str:
        try:
            if not self._page:
                return "✗ No active page"
            await self._page.wait_for_selector(selector, timeout=3000)
            await self._page.fill(selector, text)
            return f"✓ Typed: {text}"
        except Exception as e:
            try:
                if self._page:
                    await self._page.keyboard.type(text)
                    return f"✓ Typed: {text}"
            except:
                pass
            return f"✗ Failed to type: {e}"

    async def press_enter(self) -> str:
        try:
            if not self._page:
                return "✗ No active page"
            await self._page.keyboard.press("Enter")
            return "✓ Pressed Enter"
        except Exception as e:
            return f"✗ Failed: {e}"

    async def click(self, selector: str = "button, a") -> str:
        try:
            if not self._page:
                return "✗ No active page"
            await self._page.click(selector)
            return f"✓ Clicked {selector}"
        except Exception as e:
            return f"✗ Failed to click: {e}"

    async def new_tab(self) -> str:
        try:
            if not self._context:
                return "✗ No active context"
            self._page = await self._context.new_page()
            return "✓ New tab opened"
        except Exception as e:
            return f"✗ Failed: {e}"

    async def close_tab(self) -> str:
        try:
            if self._page:
                await self._page.close()
            pages = self._context.pages if self._context else []
            if pages:
                self._page = pages[-1]
            return "✓ Tab closed"
        except Exception as e:
            return f"✗ Failed: {e}"

    async def screenshot(self, path: str = "screenshot.png") -> str:
        try:
            if not self._page:
                return "✗ No active page"
            await self._page.screenshot(path=path)
            return f"✓ Screenshot saved to {path}"
        except Exception as e:
            return f"✗ Failed: {e}"
