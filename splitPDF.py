from PyPDF2 import PdfFileWriter, PdfFileReader

pdfFile = input("Enter File name");
inputpdf = PdfFileReader(open(pdfFile, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
