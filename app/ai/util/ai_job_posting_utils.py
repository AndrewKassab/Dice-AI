import openai

client = openai.Client()


def is_job_relevant(job_description, resume_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will return only true or false in regards to whether a job description "
                                          "is relevant to the provided resume. Be slightly forgiving in matching the candidate. "
                                          "The resume follows here: \n'''\n" + resume_text + "'\n'''"},
            {"role": "user", "content": "The job description is the following: \n'''\n" + job_description + "\n'''"}
        ]
    )

    response_content = response.choices[0].message.content
    if 'true' in response_content.lower():
        return True
    return False
