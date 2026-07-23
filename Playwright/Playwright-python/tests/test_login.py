from pages.login_page import LoginPage
from utils.test_data import TestData


def test_login(page):

    page.goto(TestData.URL)

    login = LoginPage(page)

    dashboard = login.login(
        TestData.USERNAME,
        TestData.PASSWORD
    )

    dashboard.verify_login_success()
