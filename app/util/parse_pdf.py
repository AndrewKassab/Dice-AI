import fitz


def parse_pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''

    for page in doc:
        text += page.get_text()

    doc.close()
    return text
