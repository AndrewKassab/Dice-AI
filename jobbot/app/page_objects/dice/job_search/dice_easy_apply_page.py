from selenium.webdriver.common.by import By

from jobbot.app.page_objects.dice.base_dice_page import BaseDicePage


class DiceEasyApplyPage(BaseDicePage):

    __NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'btn-next')]")
    __COVER_LETTER_LOCATOR = (By.XPATH, "//div[contains(@class,'cover-letter-wrapper')]")
    __RESUME_LOCATOR = (By.XPATH, "//div[contains(@class,'resume-container')]")
    __FILE_INPUT_LOCATOR = (By.ID, "fsp-fileUpload")

    def  __init__(self, driver):
        super().__init__(driver)

    def click_next_button(self):
        next_button = self.find_element(self.__NEXT_BUTTON_LOCATOR)
        next_button.click()
        return self

    def click_apply_button(self):
        apply_button = self.find_element(self.__NEXT_BUTTON_LOCATOR)
        apply_button.click()

    def upload_cover_letter(self, file_path):
        cover_letter_button = self.find_element(self.__COVER_LETTER_LOCATOR)
        cover_letter_button.click()
        self.__upload_file(file_path)
        return self

    def upload_resume(self, file_path):
        resume_button = self.find_element(self.__RESUME_LOCATOR).find_element(By.XPATH, '//button')
        resume_button.click()
        self.__upload_file(file_path)
        return self

    def __upload_file(self, file_path):
        file_input = self.find_element(self.__FILE_INPUT_LOCATOR)
        file_input.send_keys(file_path)

        upload_button = self.find_element(By.CSS_SELECTOR, "span[title='Upload']")
        upload_button.click()

    def apply_to_job(self, resume_file_path=None, cover_letter_file_path=None):
        if resume_file_path:
            self.upload_resume(resume_file_path)
        if cover_letter_file_path:
            self.upload_cover_letter(cover_letter_file_path)
        self.click_next_button()
        self.click_apply_button()
