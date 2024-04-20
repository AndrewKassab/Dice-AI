from selenium import webdriver

from app.enum.dice.search_filters.posted_date import PostedDate
from app.enum.dice.search_filters.work_settings import WorkSetting
from app.page_objects.dice.dice_login_page import DiceLoginPage
from settings import DICE_EMAIL, DICE_PASSWORD, RESUME_PATH

driver = webdriver.Chrome()

driver.get('https://www.dice.com/dashboard/login')

driver.implicitly_wait(10)

login_page = DiceLoginPage(driver)

home_feed_page = login_page.login(DICE_EMAIL, DICE_PASSWORD)

search_result_page = home_feed_page.search_job(
    'Software Engineer Developer Java Python Quality Automation', 'San Diego')

search_result_page.toggle_work_settings_option(WorkSetting.HYBRID)\
    .toggle_work_settings_option(WorkSetting.REMOTE)\
    .set_posted_date(PostedDate.LAST_7_DAYS)\
    .toggle_easy_apply()

current_index = 0

job_description_page = search_result_page.select_job_at_index(current_index)

job_description_page.click_apply_now()\
    .apply_to_job(resume_file_path=RESUME_PATH)
