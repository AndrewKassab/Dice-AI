from abc import ABC

from selenium.webdriver.remote.webelement import WebElement


class BasePageObject(ABC):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
