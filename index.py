from sys import platform
from easygui import multenterbox
from easygui import diropenbox
from easygui import fileopenbox
from PyPDF2 import PdfFileReader

pdfFile = fileopenbox()
document = PdfFileReader(pdfFile)
pages = document.getNumPages()
print(pages)
# msg = "Adicione suas credenciais do LUCCA"
# title = "NBO2001"
# fieldNames = ["Usuario","Senha"]
# fieldValues = []  # we start with blanks for the values
# fieldValues = multenterbox(msg,title, fieldNames)

# file = diropenbox()
# print(file)

# print(fieldValues)