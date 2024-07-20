from dotenv import load_dotenv
import os

from pathlib import Path

load_dotenv()

# Env Variables
DICE_EMAIL = os.environ.get('DICE_EMAIL')
DICE_PASSWORD = os.environ.get('DICE_PASSWORD')

RESUME_PATH = (Path(__file__) / 'app' / 'resources' / 'resume.pdf').resolve()
