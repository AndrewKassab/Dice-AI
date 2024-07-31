from dotenv import load_dotenv
import os

from pathlib import Path

from selenium import webdriver

from jobbot.app.enum.dice.search_filters.posted_date import PostedDate
from jobbot.app.enum.dice.search_filters.work_settings import WorkSetting

load_dotenv()

RESUME_PATH = str((Path(__file__).parent / 'app' / 'resources' / 'resume.pdf').resolve())

driver = webdriver.Chrome()
driver.implicitly_wait(3)
DRIVER_EXPLICIT_WAIT = 3

# Env Variables
DICE_EMAIL = os.environ.get('DICE_EMAIL')
DICE_PASSWORD = os.environ.get('DICE_PASSWORD')

# Dice job search configuration
POSTED_DATE = PostedDate.LAST_7_DAYS
WORK_SETTINGS_OPTIONS = [
    WorkSetting.REMOTE,
    WorkSetting.HYBRID
]
DICE_SEARCH_QUERY = "Front End Engineer"
DICE_LOCATION_QUERY = "San Diego"
