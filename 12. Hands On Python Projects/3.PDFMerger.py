from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How many pdfs you want to merge : "))

for i in range(0,n):
    name = input(f"Enter the pdf name {i+1} : ")   
    pdfs.append(name) 

for pdf in pdfs:
    print("Files:", repr(pdfs))
    print("Working directory:", __import__("os").getcwd())  
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()