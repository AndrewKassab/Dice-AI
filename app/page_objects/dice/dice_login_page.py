from selenium.webdriver.common.by import By

from app.page_objects.dice.base_dice_page import BaseDicePage
from app.page_objects.dice.dice_home_feed_page import DiceHomeFeedPage


class DiceLoginPage(BaseDicePage):

    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign In')]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        email_el = self.driver.find_element(*self.EMAIL_INPUT)
        email_el.clear()
        email_el.send_keys(email)
        return self

    def enter_password(self, password):
        password_el = self.driver.find_element(*self.PASSWORD_INPUT)
        password_el.clear()
        password_el.send_keys(password)
        return self

    def click_login_button(self):
        login_button=self.driver.find_element(*self.SIGN_IN_BUTTON)
        login_button.click()
        return DiceHomeFeedPage(self.driver)
