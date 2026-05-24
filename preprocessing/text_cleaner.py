import re


def clean_text(text):
    if text is None:
        return ""

    text = re.sub(r"<.*?>", " ", text)       # remove HTML tags
    text = re.sub(r"\s+", " ", text)         # remove extra spaces
    text = text.strip()                      # remove start/end spaces

    return text