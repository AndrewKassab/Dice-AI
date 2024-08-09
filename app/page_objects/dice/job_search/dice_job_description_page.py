from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from jobbot.app.page_objects.dice.base_dice_page import BaseDicePage
from jobbot.app.page_objects.dice.job_search.dice_easy_apply_page import DiceEasyApplyPage


class DiceJobDescriptionPage(BaseDicePage):

    __APPLY_BUTTON_LOCATOR = (By.TAG_NAME, "apply-button-wc")
    __JOB_DESCRIPTION_LOCATOR = (By.XPATH, "//section[contains(@class, 'job-description')]")

    def __init__(self, driver):
        super().__init__(driver)

    # TODO: Use __is_easy_apply to figure out what object to return
    def click_apply(self):
        apply_button = self.find_element(self.__APPLY_BUTTON_LOCATOR)
        apply_button.click()
        return DiceEasyApplyPage(self.driver)

    def get_job_description(self):
        job_description_section = self.find_element(self.__JOB_DESCRIPTION_LOCATOR)
        return job_description_section.text

    def is_apply_button_displayed(self):
        try:
            apply_button = self.find_element(self.__APPLY_BUTTON_LOCATOR)
            return apply_button.is_displayed()
        except NoSuchElementException:
            return False

    # TODO: better implementation that doesn't use text
    def __is_easy_apply(self):
        pass
