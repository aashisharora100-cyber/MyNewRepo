from playwright.sync_api import Page


class BasePage:
    """Common functionality shared by all page objects."""

    URL = "https://www.goindigo.in/"

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")
       # self._dismiss_cookie_banner()

    def _dismiss_cookie_banner(self):
        accept_btn = self.page.get_by_text("Accept", exact=True)

        if accept_btn.is_visible():
            accept_btn.click()