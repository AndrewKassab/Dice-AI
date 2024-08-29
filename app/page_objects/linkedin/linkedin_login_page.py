from selenium.webdriver.common.by import By

from dice_ai.app.page_objects.base_page import BasePage


class LinkedinLoginPage(BasePage):

    __EMAIL_INPUT = (By.ID, "username")
    __PASSWORD_INPUT = (By.ID, "password")
    __SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, email):
        email_input = self.find_element(self.__EMAIL_INPUT)
        email_input.send_keys(email)
        return self

    def set_password(self, password):
        password_input = self.find_element(self.__PASSWORD_INPUT)
        password_input.send_keys(password)
        return self

    def click_sign_in(self):
        sign_in_button = self.find_element(self.__SIGN_IN_BUTTON)
        sign_in_button.click()
        return self

    def login(self, email, password):
        self.set_email(email) \
            .set_password(password) \
            .click_sign_in()
        return LinkedinFeedPage()

