from abc import ABC

from app.page_objects.base_page_object import BasePageObject


class BasePage(ABC, BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)
