from pypdf import PdfReader

reader = PdfReader("/Users/abel/Desktop/legal_rag/data/raw_pdfs/UAE_labor_law_2021.pdf")

all_text= ""

for page in reader.pages:
    all_text += page.extract_text() + "\n"

with open("/Users/abel/Desktop/legal_rag/data/extracted_text/UAE_labor_law_2021.txt", "w", encoding="utf-8") as file:
    file.write(all_text)
