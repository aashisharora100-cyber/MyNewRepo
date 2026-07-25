from playwright.sync_api import Page
from .base_page import BasePage
from .flight_search_page import FlightSearchPage


class HomePage(BasePage):
    """goindigo.in landing page containing the Booking Widget."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.booking_widget = page.get_by_role("main", name="Booking Widget")


    def open_flight_search(self):
        self.goto()
        return FlightSearchPage(self.page)
