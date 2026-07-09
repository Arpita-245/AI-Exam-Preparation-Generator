import os

from app.utils.pdf_reader import extract_pdf_text
from app.utils.docx_reader import extract_docx_text
from app.utils.text_cleaner import clean_text


def process_document(filepath):

    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".pdf":

        text = extract_pdf_text(filepath)

    elif extension == ".docx":

        text = extract_docx_text(filepath)

    elif extension == ".txt":

        with open(filepath, "r", encoding="utf-8") as file:

            text = file.read()

    else:

        return ""

    return clean_text(text)