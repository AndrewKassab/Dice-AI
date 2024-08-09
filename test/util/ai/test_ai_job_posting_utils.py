from pathlib import Path
import fitz
from unittest import TestCase
from jobbot.app.util.parse_pdf import parse_pdf_to_text

current_script_path = Path(__file__).parent.parent.parent
resources_path = current_script_path / 'resources' / 'test_resume.pdf'
resume_path = resources_path.resolve()

valid_job_description = "Location: Remote | Must sit in ID, OR, WA, CA, UT, AZ, NV , CO Employment Type: 12-month contract to hire  Pay Range: $55-65 / hr Benefits: Medical insurance, 401K, sick leave, and employee assistance program. Depending on your package selection, Averro offers PTO, paid holidays, dental/vision, pet, and legal insurance. Role & Responsibilities: We are currently seeking a talented and experienced Software QA Engineer to join our team! This is an excellent opportunity for individuals with 3-5 years of experience in QA testing, particularly those who excel in creating test plans using Azure DevOps (ADO) and possess proficiency in automation tools such as Selenium and/or Pytest. The successful candidate will contribute to the advancement of their career in the dynamic field of software quality assurance.  Key Responsibilities:  Develop and execute comprehensive test plans in Azure DevOps (ADO). Utilize automation tools, specifically Selenium and/or Pytest, to enhance testing efficiency. Conduct Python scripting to automate test scenarios and improve testing processes. Collaborate with cross-functional teams to ensure the delivery of high-quality software products. Integrate continuous integration tools such as Jenkins/ADO and GIT into the testing process. Essential Qualifications:  3-5 years of experience in software quality assurance and testing. Proven expertise in creating and implementing test plans using Azure DevOps (ADO). Hands-on experience with automation tools, specifically Selenium and/or Pytest. Proficiency in Python scripting for test automation. Familiarity with continuous integration tools like Jenkins/ADO and GIT. Bonus Qualifications:  Additional experience with other automation tools or programming languages. Certification in software testing (e.g., ISTQB). WHY AVERRO? Averro is a Veteran-Owned organization dedicated to delivering innovative talent solutions and technology services. Our commitment to values like curiosity, trust-building, and empowerment reflects in our client satisfaction, timely support, and unmatched consultant care. Join us on a journey of professional growth, where your skills and contributions are valued.  Averro is an equal opportunity employer, fostering diversity, equity, and inclusion. All qualified applicants will be considered for employment, irrespective of backgrounds, consistent with legal obligations. We celebrate the unique perspectives each team member brings, contributing to an inclusive workplace. Your career ascent begins with Averro!"
doc = fitz.open()
resume_text = parse_pdf_to_text(resume_path)


class AiJobPostingUtilsTest(TestCase):
    pass
