from docx import Document
import os
from docx2pdf import convert

word_path = "empty.docx"
pdf_path = "empty.pdf"

# convert(word_path, pdf_path)



try:
    os.mknod('newfile.txt')
except FileExistsError as e:
    print(f'An error occurred: {e}')





# wordDoc = Document("resume.docx")

# word = comtypes.client.CreateObject("Word.Application")
# docx_path = os.path.abspath(word_path)
# pdf_path = os.path.abspath(pdf_path)

# pdf_format = 17
# word.Visible = False
# doc = word.Documents.Open(docx_path)
# in_file.SaveAs(pdf_path, FileFormat=pdf_format)
# in_file.Close()

# word.Quit()