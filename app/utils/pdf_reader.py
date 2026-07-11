import PyPDF2


def extract_pdf_text(filepath):

    text = ""

    with open(filepath, "rb") as pdf:

        reader = PyPDF2.PdfReader(pdf)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text