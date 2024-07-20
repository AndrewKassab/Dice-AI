from abc import ABC

from jobbot.app.page_objects.base_page import BasePage


class BaseDicePage(BasePage, ABC):

    def __init__(self, driver):
        super().__init__(driver)
