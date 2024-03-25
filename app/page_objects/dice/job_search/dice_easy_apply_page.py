from selenium.webdriver.common.by import By

from app.page_objects.dice.base_dice_page import BaseDicePage


class DiceEasyApplyPage(BaseDicePage):

    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'btn-next')]")
    COVER_LETTER_LOCATOR = (By.XPATH, "//div[contains(@class,'cover-letter') and contains(@class, 'file-picker-wrapper')]")
    FILE_INPUT_LOCATOR = (By.ID, "fsp-fileUpload")

    def  __init__(self, driver):
        super.__init__(driver)

    def click_next_button(self):
        next_button = self.find_element(self.NEXT_BUTTON_LOCATOR)
        next_button.click()
        return self

    def click_apply_button(self):
        apply_button = self.find_element(self.NEXT_BUTTON_LOCATOR)
        apply_button.click()
        # TODO: Return other driver tab?

    def upload_cover_letter(self, file_path):
        cover_letter_button = self.find_element(self.COVER_LETTER_LOCATOR)
        cover_letter_button.click()
        self.__upload_file(file_path)
        return self

    def __upload_file(self, file_path):
        file_input = self.find_element(self.FILE_INPUT_LOCATOR)
        file_input.send_keys(file_path)

        upload_button = self.find_element(By.CSS_SELECTOR, "span[title='Upload']")
        upload_button.click()
