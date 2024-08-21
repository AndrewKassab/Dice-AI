from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from jobbot.app.enum.linkedin.linkedin_date_posted import LinkedinDatePosted
from jobbot.app.page_objects.linkedin.base_linkedin_page import BaseLinkedinPage


class LinkedinJobsPage(BaseLinkedinPage):

    __JOB_SEARCH_QUERY_FIELD = (By.XPATH, "//input[@id[contains(.,'jobs-search-box-keyword')]]")
    __JOB_SEARCH_LOCATION_FIELD = (By.XPATH, "//input[@id[contains(.,'jobs-search-box-location')]]")
    __JOB_LIST_ITEM = (By.XPATH, "//li[contains(@class, 'jobs-search-results__list-item')]")
    __DATE_POSTED_FILTER = (By.ID, "searchFilter_timePostedRange")
    __DATE_POSTED_FILTER_OPTIONS = (By.CSS_SELECTOR, "input[name='date-posted-filter-value']")
    __EASY_APPLY_FILTER = (By.CSS_SELECTOR, "button[aria-label='Easy Apply filter.']")
    __WORK_SETTING_FILTER_OPTIONS = (By.CSS_SELECTOR, "input[name='remote-filter-value']")

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

    def select_job_at_index(self, index):

    def set_date_posted_filter(self, date_posted_filter: LinkedinDatePosted):



