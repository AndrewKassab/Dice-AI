from dotenv import load_dotenv
import os

from pathlib import Path

from jobbot.app.enum.dice.search_filters.posted_date import PostedDate
from jobbot.app.enum.dice.search_filters.work_settings import WorkSetting

load_dotenv()

# Env Variables
DICE_EMAIL = os.environ.get('DICE_EMAIL')
DICE_PASSWORD = os.environ.get('DICE_PASSWORD')

RESUME_PATH = str((Path(__file__).parent / 'app' / 'resources' / 'resume.pdf').resolve())

# Dice job search configuration
POSTED_DATE = PostedDate.LAST_7_DAYS
WORK_SETTINGS_OPTIONS = [
    WorkSetting.REMOTE,
    WorkSetting.HYBRID
]
