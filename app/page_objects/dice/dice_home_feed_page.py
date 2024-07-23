from selenium.webdriver.common.by import By

from jobbot.app.page_objects.dice.base_dice_page import BaseDicePage
from jobbot.app.page_objects.dice.job_search.dice_job_search_bar import DiceJobSearchBar
from jobbot.app.page_objects.dice.job_search.dice_job_search_result_page import DiceJobSearchResultPage


class DiceHomeFeedPage(BaseDicePage):

    def __init__(self, driver):
        super().__init__(driver)
        popup_exit_button = self.find_element((By.ID, 'sms-close'))
        if popup_exit_button.is_displayed():
            popup_exit_button.click()
        self.search_bar = DiceJobSearchBar(driver)

    def search_job(self, search_term, location) -> DiceJobSearchResultPage:
        return self.search_bar.set_search_term(search_term)\
            .set_location(location)\
            .click_search()
