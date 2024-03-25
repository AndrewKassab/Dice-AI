from selenium.webdriver.common.by import By

from app.page_objects.dice.base_dice_page import BaseDicePage
from app.page_objects.dice.job_search.dice_easy_apply_page import DiceEasyApplyPage


class DiceJobDescriptionPage(BaseDicePage):

    def __init__(self, driver):
        super.__init__(driver)

    def click_apply_now(self):
        is_easy_apply = self.__is_easy_apply()
        apply_button = self.find_element((By.ID, 'applyButton'))
        apply_button.click()
        if is_easy_apply:
            return DiceEasyApplyPage()

    def get_job_description(self):
        job_description_section = self.find_element((By.XPATH, "//section[contains(@class, 'job-description')]"))
        return job_description_section.text

    # TODO: better implementation
    def __is_easy_apply(self):
        return self.find_element((By.XPATH, "//*[contains(text(),'Easy Apply')]"))
