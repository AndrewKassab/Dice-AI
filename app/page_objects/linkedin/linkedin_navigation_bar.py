from selenium.webdriver.common.by import By

from jobbot.app.enum.linkedin.linkedin_nav_item import LinkedinNavItem
from jobbot.app.page_objects.base_page_object import BasePageObject
from jobbot.app.page_objects.linkedin.jobs.linkedin_jobs_page import LinkedinJobsPage


class LinkedinNavBar(BasePageObject):

    def __init(self, driver):
        super().__init__(driver)

    def __open_page(self, nav_bar_page: LinkedinNavItem):
        anchor = self.find_element((By.CSS_SELECTOR, f"span[title='{nav_bar_page.value}']"))
        anchor.click()

    def open_jobs_page(self):
        self.__open_page(LinkedinNavItem.JOBS)
        return LinkedinJobsPage()


