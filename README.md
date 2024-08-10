# Job-Bot (v1)
Job-bot is a program that helps with the grueling process of job-hunting by automating it away.
If employers are using automation and AI tools to assist in their application process, then why shouldn't we?

Job-bot uses Selenium in combination with OpenAI's api to automate browser interactions related to job applications. 
OpenAI's gpt4-o model is used to write cover letters and determine whether a job is relevant to the applicant in question. 

Job-Bot is able to apply to Easy-Apply jobs on [Dice](https://dice.com) based on a search query and filter parameters.
If the setting is activated, it will leverage AI to write cover letters catered to the job description. In the future, 
if current capabilities allow, there are plans to add support for applications that aren't Easy-Apply through integration
with another Selenium-AI library I am creating here: [Selenium Python with AI](https://github.com/AndrewKassab/selenium_ai)

# Setup

The setup does consist of several steps, they should be rather simple, but just require some patience.
For starters, make sure to clone the repository locally and enter the root directory.

**Settings.py** (in root)

USE_AI is set to False by default, but you'll get better results setting it to True, which enables
the auto Cover-Letter writing feature. If setting to True, you'll need to have the 'OPENAI_API_KEY' env 
variable set. I will explain more about this later. 

Be sure to set the search configuration values on the bottom. These should be self-explanatory

**Environment Variables** (dotenv supported):

- DICE_EMAIL: Email address for your dice account.
- DICE_PASSWORD: Password for your dice account.
- OPENAI_API_KEY (optional): API Key for billing your OpenAI account (more on this later)

**Resume**

Copy your current resume (as a pdf) over to /app/resources, and make sure to rename it to resume.pdf.

**Chrome Driver**

In order to use Selenium, you need to have Chrome Driver (and Chrome) installed on your computer and 
the executable must be added to your path. 

TO BE CONTINUED.



