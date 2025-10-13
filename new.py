import PyPDF2
with open('RESUME.pdf', 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

print(text)