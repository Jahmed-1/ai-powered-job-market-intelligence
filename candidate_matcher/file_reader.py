import pdfplumber
from docx import Document


def read_txt_file(uploaded_file):
    return uploaded_file.read().decode("utf-8")


def read_pdf_file(uploaded_file):
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def read_docx_file(uploaded_file):
    document = Document(uploaded_file)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def read_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return read_txt_file(uploaded_file)

    elif file_name.endswith(".pdf"):
        return read_pdf_file(uploaded_file)

    elif file_name.endswith(".docx"):
        return read_docx_file(uploaded_file)

    else:
        return ""