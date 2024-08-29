from selenium.webdriver.common.by import By

from dice_ai.app.page_objects.base_page_object import BasePageObject
from dice_ai.app.page_objects.dice.job_search.dice_job_search_result_page import DiceJobSearchResultPage


class DiceJobSearchBar(BasePageObject):

    __SEARCH_TERM = (By.ID, 'typeaheadInput')
    __LOCATION = (By.ID, 'google-location-search')
    __SEARCH_BUTTON = (By.ID, 'submitSearch-button')

    def __init__(self, driver):
        super().__init__(driver)

    def set_search_term(self, text):
        search_term_el = self.find_element(self.__SEARCH_TERM)
        search_term_el.clear()
        search_term_el.send_keys(text)
        return self

    def set_location(self, location):
        location_el = self.find_element(self.__LOCATION)
        location_el.clear()
        location_el.send_keys(location)
        return self

    def click_search(self) -> DiceJobSearchResultPage:
        search_button_el = self.find_element(self.__SEARCH_BUTTON)
        search_button_el.click()
        return DiceJobSearchResultPage(self.driver)
