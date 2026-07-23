from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.success_message = page.locator(".post-title")

    def verify_login_success(self):
        expect(self.success_message).to_have_text("Logged In Successfully")