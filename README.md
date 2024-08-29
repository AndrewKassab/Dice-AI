# Job-Bot (v1)
Job-bot is a program that helps with the grueling process of job-hunting by automating it away.
If employers are using automation and AI tools to assist in their application process, then why shouldn't we?

Job-bot uses Selenium in combination with OpenAI's api to automate browser interactions related to job applications. 
OpenAI's gpt4-o model is used to write cover letters based on the job description.

# Current Features

* Applies to Easy-Apply jobs on [Dice](https://dice.com) based on search query and filter parameters
* Leverages AI to write cover letters catered to the job descripotion.

# Planned Features

* Support for External job applications on Dice that don't use Easy Apply
* Support for Linkedin (both Easy Apply / External)
  
# Setup

The setup does consist of several steps, they should be rather simple, but just require some patience.
For starters, make sure to clone the repository locally and enter the root directory.

**Settings.py** (in root)

`USE_AI` is set to True by default unless there is no API key (in which case it will default to `False`)
which enables the auto Cover-Letter writing feature. You'll need to have the `OPENAI_API_KEY` env variable
set. I will explain more about this later.

Be sure to set the search configuration values on the bottom. These should be self-explanatory

**Environment Variables** (dotenv supported):

- DICE_EMAIL: Email address for your dice account.
- DICE_PASSWORD: Password for your dice account.
- OPENAI_API_KEY (optional): API Key for billing your OpenAI account (more on this later)

**Resume**

Copy your current resume (as a pdf) over to /app/resources, and make sure to rename it to resume.pdf.

**Chrome Driver**

In order to use Selenium, you need to have Chrome Driver (and Chrome) installed on your computer and 
the executable must be added to your path. Search for OS specific instructions on how to add the 
executable to your PATH.

[Installing Chrome Driver](https://developer.chrome.com/docs/chromedriver/get-started)

**OpenAI**

If you'd like to use the AI features, you'll need an API key and some API credits. Don't worry, the
amount of credits this program uses is fairly low. In my experience, I've only seen about 1 cent of 
credits get used over 30 applications. On [OpenAI](https://platform.openai.com/settings/profile) make
your way to the Billing section to add some credits to use. Then get an API key on the 'Your Profile' 
tab and add it to your environment variables or .env file as OPENAI_API_KEY.

**Python** 

Make sure you're using Python3.8 or above, and download the requirements using 
`python -m pip install -r requirements.txt` from the root folder of the project.

**Running**

After you're done setting up, go ahead and run `app/bot/auto_apply_dice.py` and a Chrome browser should
open up and begin applying to jobs for you with the specified query. Make sure you don't interfere with 
this browser.




