import os

import openai
from fpdf import FPDF
from unidecode import unidecode

client = openai.Client()


def write_cover_letter_as_pdf(job_description, resume_text, output_path):
    """Leverages openAI's API to write a cover letter for the job using the provided resume"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Please write a short cover letter using the information from the provided "
                                          "resume and job description. Please skip identifying information as it will "
                                          "already be included in the resume. "
                                          "The resume follows here: \n'''\n" + resume_text + "'\n'''"},
            {"role": "user", "content": "The job description is the following: \n'''\n" + job_description + "\n'''"}
        ]
    )

    response_content = unidecode(response.choices[0].message.content)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, response_content)

    if os.path.exists(output_path):
        os.remove(output_path)

    pdf.output(output_path)

