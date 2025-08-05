import pdfplumber
import re

def clean_text(text):
    # Remove non-ASCII characters and extra whitespace
    text = re.sub(r'\s+', ' ', text)  # normalize whitespace
    return text.strip()

def pdf_to_clean_txt(pdf_path, txt_path):
    all_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw_text = page.extract_text()
            if raw_text:
                cleaned = clean_text(raw_text)
                all_text += cleaned + "\n"

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(all_text)

# Example usage
pdf_to_clean_txt("notes/Le Parasite.pdf", "output.txt")

