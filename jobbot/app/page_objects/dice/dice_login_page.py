from selenium.webdriver.common.by import By

from jobbot.app.page_objects.dice.base_dice_page import BaseDicePage
from jobbot.app.page_objects.dice.dice_home_feed_page import DiceHomeFeedPage


class DiceLoginPage(BaseDicePage):

    __EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name=email]')
    __PASSWORD_INPUT = (By.ID, 'password')
    __SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_el = self.driver.find_element(*self.__EMAIL_INPUT)
        email_el.clear()
        email_el.send_keys(email)
        return self

    def enter_password(self, password):
        password_el = self.driver.find_element(*self.__PASSWORD_INPUT)
        password_el.clear()
        password_el.send_keys(password)
        return self

    def click_login_button(self) -> DiceHomeFeedPage:
        login_button=self.driver.find_element(*self.__SIGN_IN_BUTTON)
        login_button.click()
        return DiceHomeFeedPage(self.driver)

    def login(self, email, password) -> DiceHomeFeedPage:
        return self.enter_email(email)\
            .enter_password(password)\
            .click_login_button()
