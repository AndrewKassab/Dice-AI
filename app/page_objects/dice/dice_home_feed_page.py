from app.page_objects.dice.base_dice_page import BaseDicePage
from app.page_objects.dice.job_search.dice_job_search_bar import DiceJobSearchBar


class DiceHomeFeedPage(BaseDicePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = DiceJobSearchBar(driver)

    def search_job(self, search_term, location):
        self.search_bar.set_search_term(search_term)\
            .set_location(location)
        return self.search_bar.click_search()
