from typing import Optional

import openai
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_ai.app.driver.ai_web_element import AiWebElement


class AiWebDriver(WebDriver):
    ''' Currently only works for Chrome / automatically assumes we are using chrome'''

    def __init__(self):
        super().__init__()
        self.ai_client = openai.Client()

    def find_element(self, by=By.ID, value: Optional[str] = None) -> AiWebElement:
        '''
        Overrides the parent method, but behaves as usual unless an element isn't found

        If an element is not found, we will attempt one more time by leveraging AI to find
        what it thinks is the nearest matching element.
        '''
        try:
            return super().find_element(by, value)
        except NoSuchElementException:
            query = ""

    def find_element_with_description(self, element_description: str) -> AiWebElement:
        '''
        Attempts to leverage AI to find the element in question
        :return:
        '''
        pass
