import logging

from dotenv import load_dotenv
import os

from pathlib import Path

from selenium import webdriver

from jobbot.app.enum.dice.search.posted_date import PostedDate
from jobbot.app.enum.dice.search.work_settings import WorkSetting
from jobbot.app.util.parse_pdf import parse_pdf_to_text

load_dotenv()

resources_path = (Path(__file__).parent / 'app' / 'resources')
RESUME_PATH = str((resources_path / 'resume.pdf').resolve())
COVER_LETTER_PATH = str((resources_path / 'cover_letter.pdf').resolve())

try:
    RESUME_TEXT = parse_pdf_to_text(RESUME_PATH)
except:
    logging.error('Error parsing resume, are you sure there is a resume.pdf in app/resources?')

driver = webdriver.Chrome()
driver.implicitly_wait(2)
DRIVER_EXPLICIT_WAIT = 2

# Activates Job description matching and cover letter writing but requires the
# OPENAI_APY_KEY environment variable to be set.
USE_AI = True
if os.environ.get('OPENAI_API_KEY') is None:
    USE_AI = False

# Env Variables
DICE_EMAIL = os.environ.get('DICE_EMAIL')
DICE_PASSWORD = os.environ.get('DICE_PASSWORD')

# Dice job search configuration, set to preferences.
POSTED_DATE = PostedDate.LAST_7_DAYS
WORK_SETTINGS_OPTIONS = [
    WorkSetting.REMOTE,
    #WorkSetting.HYBRID,
    #WorkSetting.ON_SITE,
]
DICE_SEARCH_QUERY = ""
DICE_LOCATION_QUERY = ""
