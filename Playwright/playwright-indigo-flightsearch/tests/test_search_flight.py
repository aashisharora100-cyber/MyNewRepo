from pages.home_page import HomePage


def test_one_way_delhi_to_mumbai_search(page):

    home = HomePage(page)

    flight_search = home.open_flight_search()

    #flight_search.select_one_way()

    flight_search.select_origin("Delhi")

    #flight_search.select_destination("Mumbai")

    # flight_search.click_search()

    #page.wait_for_url("**/flight-select*", timeout=15000)

    #assert "flight-select" in page.url