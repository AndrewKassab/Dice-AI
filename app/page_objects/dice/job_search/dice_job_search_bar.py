from selenium.webdriver.common.by import By

from app.page_objects.base_page_object import BasePageObject
from app.page_objects.dice.job_search.dice_job_search_result_page import DiceJobSearchResultPage


class DiceJobSearchBar(BasePageObject):

    SEARCH_TERM = (By.ID, 'typeaheadInput')
    LOCATION = (By.ID, 'google-location-search')
    SEARCH_JOBS_BUTTON = (By.ID, 'submitSearch-button')

    def __init__(self, driver):
        super().__init__(driver)

    def set_search_term(self, text):
        search_term_el = self.find_element(self.SEARCH_TERM)
        search_term_el.clear()
        search_term_el.send_keys(text)
        return self

    def set_location(self, location):
        location_el = self.find_element(self.LOCATION)
        location_el.clear()
        location_el.send_keys(location)
        return self

    def click_search(self):
        search_button_el = self.find_element(self.SEARCH_BUTTON)
        search_button_el.click()
        return DiceJobSearchResultPage()
