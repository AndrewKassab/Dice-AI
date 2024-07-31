from jobbot.app.page_objects.dice.dice_login_page import DiceLoginPage
from jobbot.settings import DICE_EMAIL, DICE_PASSWORD, RESUME_PATH, POSTED_DATE, WORK_SETTINGS_OPTIONS, \
    DICE_SEARCH_QUERY, DICE_LOCATION_QUERY, driver

driver.get('https://www.dice.com/dashboard/login')

driver.implicitly_wait(10)

login_page = DiceLoginPage(driver)

home_feed_page = login_page.login(DICE_EMAIL, DICE_PASSWORD)

search_result_page = home_feed_page.search_job(DICE_SEARCH_QUERY, DICE_LOCATION_QUERY)

for option in WORK_SETTINGS_OPTIONS:
    search_result_page.toggle_work_settings_option(option)

search_result_page.set_posted_date(POSTED_DATE)\
    .toggle_easy_apply()

current_index = 0

while current_index < search_result_page.get_number_of_jobs_on_page():
    # In case we've already applied to this role
    if not search_result_page.is_job_at_index_applied(current_index):
        job_description_page = search_result_page.select_job_at_index(current_index)

        job_description_page.click_apply() \
            .apply_to_job(resume_file_path=RESUME_PATH)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    current_index += 1

