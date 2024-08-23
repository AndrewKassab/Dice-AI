from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from jobbot.app.enum.linkedin.linkedin_date_posted import LinkedinDatePosted
from jobbot.app.enum.linkedin.linkedin_work_settings import LinkedinWorkSetting
from jobbot.app.page_objects.linkedin.base_linkedin_page import BaseLinkedinPage
from jobbot.app.page_objects.linkedin.jobs.linkedin_application_modal import LinkedinApplicationModal


class LinkedinJobsPage(BaseLinkedinPage):

    __JOB_SEARCH_QUERY_FIELD = (By.XPATH, "//input[@id[contains(.,'jobs-search-box-keyword')]]")
    __JOB_SEARCH_LOCATION_FIELD = (By.XPATH, "//input[@id[contains(.,'jobs-search-box-location')]]")
    __JOB_LIST_ITEMS = (By.XPATH, "//li[contains(@class, 'jobs-search-results__list-item')]")
    __DATE_POSTED_FILTER_OPTIONS = (By.CSS_SELECTOR, "input[name='date-posted-filter-value']")
    __EASY_APPLY_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Easy Apply filter.']")
    __WORK_SETTING_FILTER_OPTIONS = (By.CSS_SELECTOR, "input[name='remote-filter-value']")
    __ALL_FILTERS_BUTTON = (By.CSS_SELECTOR, "div[class='relative mr2']")
    __SHOW_RESULTS_BUTTON = (By.CSS_SELECTOR, "button[data-test-reusables-filters-modal-show-results-button='true']")
    __APPLY_BUTTON = (By.XPATH, "//button[contains(@class,'jobs-apply-button')]")

    def __init__(self, driver):
        super().__init__(driver)

    def set_search_query(self, search_query):
        search_query_field = self.find_element(self.__JOB_SEARCH_QUERY_FIELD)
        search_query_field.send_keys(search_query)
        return self

    def set_search_location(self, search_location):
        search_location_field = self.find_element(self.__JOB_SEARCH_LOCATION_FIELD)
        search_location_field.send_keys(search_location)
        return self

    def update_search_results(self):
        search_query_field = self.find_element(self.__JOB_SEARCH_QUERY_FIELD)
        search_query_field.click()
        search_query_field.send_keys(Keys.ENTER)
        return self

    def select_job_at_index(self, index):
        job_list_items = self.find_elements(self.__JOB_LIST_ITEMS)
        job_list_items[index].click()
        return self

    def set_filters(self, date_posted_filter: LinkedinDatePosted, work_setting_filters: [LinkedinWorkSetting]):
        all_filters_button = self.find_element(self.__ALL_FILTERS_BUTTON)
        all_filters_button.click()

        date_posted_filter_options = self.find_elements(self.__DATE_POSTED_FILTER_OPTIONS)
        date_posted_filter_options[date_posted_filter.value].click()

        work_setting_filter_options = self.find_elements(self.__WORK_SETTING_FILTER_OPTIONS)
        for work_setting in work_setting_filters:
            work_setting_filter_options[work_setting.value].click()

        show_results_button = self.find_element(self.__SHOW_RESULTS_BUTTON)
        show_results_button.click()
        return self

    def select_easy_apply(self):
        easy_apply_button = self.find_element(self.__EASY_APPLY_BUTTON)
        easy_apply_button.click()
        return self

    def click_page(self, page_number):
        try:
            page_button = self.find_element((By.CSS_SELECTOR, f"button[aria-label='Page {page_number}']"))
            page_button.click()
            return self
        except NoSuchElementException:
            return False

    def click_apply(self):
        try:
            apply_button = self.find_element(self.__APPLY_BUTTON)
            apply_button.click()
            return LinkedinApplicationModal()
        except NoSuchElementException:
            return False
