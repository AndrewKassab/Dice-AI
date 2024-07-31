from abc import ABC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jobbot.settings import DRIVER_EXPLICIT_WAIT


class BasePageObject(ABC):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element_wait_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=DRIVER_EXPLICIT_WAIT).until(
            EC.element_to_be_clickable(locator)
        )
