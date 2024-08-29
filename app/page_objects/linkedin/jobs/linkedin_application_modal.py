from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from dice_ai.app.enum.linkedin.linkedin_question_type import LinkedinQuestionType
from dice_ai.app.page_objects.base_page_object import BasePageObject


class LinkedinApplicationModal(BasePageObject):

    __NEXT_BUTTON = (By.XPATH, "//button[@data-easy-apply-next-button]")
    __FILE_INPUT = (By.CSS_SELECTOR, "input[name='file']")
    __ADDITIONAL_QUESTIONS = (By.XPATH, "//div[contains(@class,'jobs-easy-apply-form-section__grouping')]")
    __QUESTION_LABEL_CHILD = (By.XPATH, ".//label[@class='artdeco-text-input--label']")
    __QUESTION_INPUT = (By.XPATH, ".//input")
    __RADIO_SEL_QUESTION_TITLE_CHILD = (By.XPATH, ".//span[contains(@class,'fb-dash-form-element__label')]")
    __RADIO_INPUT_CHILD_YES = (By.XPATH, ".//input[@data-test-text-selectable-option__input='Yes']")
    __RADIO_INPUT_CHILD_NO = (By.XPATH, ".//input[@data-test-text-selectable-option__input='No']")
    __REVIEW_BUTTON = (By.XPATH, "//button[@aria-label='Review your application']")
    __SUBMIT_BUTTON = (By.XPATH, "//button[@aria-label='Submit application']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_next(self):
        try:
            next_button = self.find_element(self.__NEXT_BUTTON)
            next_button.click()
            return self
        except NoSuchElementException:
            return False

    def click_review(self):
        try:
            review_button = self.find_element(self.__REVIEW_BUTTON)
            review_button.click()
            return self
        except NoSuchElementException:
            return False

    def click_submit(self):
        submit_button = self.find_element(self.__SUBMIT_BUTTON)
        submit_button.click()

    def upload_resume(self, resume_path):
        try:
            file_input = self.find_element(self.__FILE_INPUT)
            file_input.send_keys(resume_path)
            return self
        except NoSuchElementException:
            return False

    def get_question_at_index(self, index) -> (LinkedinQuestionType, str):
        questions = self.find_elements(self.__ADDITIONAL_QUESTIONS)
        if len(questions) <= index:
            return False
        question_at_index = questions.get(index)

        if self.__is_input_question(question_at_index):
            question_text = question_at_index.find_element(self.__QUESTION_LABEL_CHILD).text
            return [LinkedinQuestionType.INPUT, question_text]
        else:
            question_text = question_at_index.find_element(self.__RADIO_SEL_QUESTION_TITLE_CHILD).text
            if self.__is_radio_question(question_at_index):
                return (LinkedinQuestionType.RADIO, question_text)

    def __is_input_question(self, question):
        return len(question.find_elements(self.__QUESTION_LABEL_CHILD)) > 0

    def __is_radio_question(self, question):
        return len(question.find_elements(self.__RADIO_INPUT_CHILD_NO)) > 0

    def __get_select_options(self, question):
        options_elements = question.find_elements(".//option")
        options = []
        for option in options_elements:
            options.append(option.text)
        return options

    def fill_question_at_index(self, index, question_type : LinkedinQuestionType, response):
        questions = self.find_elements(self.__ADDITIONAL_QUESTIONS)
        question_at_index = questions.get(index)
        if question_type == LinkedinQuestionType.INPUT:
            pass
        elif question_type == LinkedinQuestionType.RADIO:
            pass
        else:
            pass



