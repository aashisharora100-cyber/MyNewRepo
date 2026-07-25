from playwright.sync_api import Page
from .base_page import BasePage


class FlightSearchPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.one_way_radio = page.get_by_role("radio", name="oneWay")

        self.origin_button = page.get_by_role("button", name="sourceCity")

        self.destination_button = page.get_by_role("button", name="destinationCity")

        self.city_search_box = page.get_by_role("combobox", name="Start typing..")

        self.search_button = page.get_by_role("button", name="Search", exact=True)

    #def select_one_way(self):
        #self.one_way_radio.check(force=True)

    def select_origin(self, city):
        self.origin_button.click()
        self.city_search_box.fill(city)
        self.page.get_by_text(city, exact=False).first.click()

    def select_destination(self, city):
        self.destination_button.click()
        self.city_search_box.fill(city)
        self.page.get_by_text(city, exact=False).first.click()

    def click_search(self):
        self.search_button.click()