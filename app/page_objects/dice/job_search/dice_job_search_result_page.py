from selenium.webdriver.common.by import By

from app.enum.dice.search_filters.employment_type import EmploymentType
from app.enum.dice.search_filters.posted_date import PostedDate
from app.enum.dice.search_filters.work_settings import WorkSetting
from app.page_objects.dice.base_dice_page import BaseDicePage
from app.page_objects.dice.job_description_page import DiceJobDescriptionPage


class DiceJobSearchResultPage(BaseDicePage):

    JOB_LINKS_LOCATOR = (By.XPATH, "//a[@data-cy='card-title-link']")
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//a[contains(text(),'»')]")

    def __init__(self, driver):
        super().__init__(driver)

    def toggle_work_settings_option(self, work_setting: WorkSetting):
        list_element = self.find_element((By.XPATH, f"//button[aria-label='Filter Search Results by {work_setting.value}']"))
        list_element.click()
        return self

    def set_posted_date(self, posted_date: PostedDate):
        posted_date_element = self.find_element((By.XPATH, f"//button[contains(text(),'{posted_date.value}')]"))
        posted_date_element.click()
        return self

    def toggle_employment_type(self, employment_type: EmploymentType):
        employment_type_element = self.find_element((By.XPATH, f"//button[aria-label='Filter Search Results by {employment_type.value}']"))
        employment_type_element.click()
        return self

    def toggle_easy_apply(self):
        easy_apply_element = self.find_element((By.XPATH, f"//button[aria-label='Filter Search Results by Easy Apply']"))
        easy_apply_element.click()
        return self

    def get_number_of_jobs_on_page(self):
        job_links = self.find_elements(self.JOB_LINKS_LOCATOR)
        return len(job_links)

    def select_job_at_index(self, index):
        job_links = self.find_elements(self.JOB_LINKS_LOCATOR)
        job_links[index].click()
        return DiceJobDescriptionPage()

    def click_next_page(self):
        next_page_element = self.find_element(self.NEXT_BUTTON_LOCATOR)
        next_page_element.click()
        return DiceJobSearchResultPage()
