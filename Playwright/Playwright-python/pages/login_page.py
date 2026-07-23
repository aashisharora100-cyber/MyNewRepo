from pages.dashboard_page import DashboardPage

class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username = page.locator("#username")   #storing in locator object
        self.password =  page.locator("#password")
        self.login_button =  page.locator("#submit")

    def enter_username(self, user):
        self.username.fill(user)    #using the locator object

    def enter_password(self, pwd):
        self.password.fill(pwd)

    def click_login(self):
        self.login_button.click()

    def login(self, user, pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()

        return DashboardPage(self.page)