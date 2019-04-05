import PyPDF4
pdfFileObj = open('demopdf.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
pageObj.extractText()
