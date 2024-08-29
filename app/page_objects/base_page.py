from abc import ABC

from dice_ai.app.page_objects.base_page_object import BasePageObject


class BasePage(BasePageObject, ABC):

    def __init__(self, driver):
        super().__init__(driver)
