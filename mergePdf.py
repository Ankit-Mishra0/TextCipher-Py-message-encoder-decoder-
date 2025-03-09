from pypdf import PdfWriter
import os
import platform

def findPdf(fileName,searcDir=None):
    if not fileName.lower().endswith(".pdf"):
        fileName += ".pdf" 
    if searcDir is None:
        if platform.system()=="Windows":
            searcDir="C:\\"
        else:
            searcDir="/Users"
    for root, dirs, files in os.walk(searcDir):
        if fileName in files:
            return os.path.join(root,fileName)
    return None
    
def mergePdf(pdfs,output):
    pdf_writer = PdfWriter()

    for pdf in pdfs:
        pdf_writer.append(pdf)

    with open(output, "wb") as f:
        pdf_writer.write(f)
        print(f"\n Merged PDF saved as: {output}")
    


try:
    n=int(input("enter Number of pdfs to be merged: "))
except ValueError:
    print("Enter a valid number of pdfs to be emrged ")
    exit()
else:
    if n<=1:
        print("Enter a valid Number of pdfs to be merged")
        exit()
pdfs=[]
for i in range(n):
    pdfName=input(f"Enter the name of pdf {i+1} (with or without .pdf extension) :")
    pdfPath=findPdf(pdfName)
    if(pdfPath):
        print(f"{pdfName} found")
        pdfs.append(pdfPath)
    else:
        print(f"pdf with name {pdfName} not found")
        exit()
output=input("Enter the name of final pdf: ")
if not output.lower().endswith(".pdf"):
        output += ".pdf" 
outputPath=os.path.join(os.getcwd(),output)
if not pdfs:
    print("no valid pdf found to be merged")
    exit()
mergePdf(pdfs,outputPath)

