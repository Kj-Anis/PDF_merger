import os
import pypdf

merger = pypdf.PdfWriter()
pdf_store = []

def pdf_merger(name):
    merger.write(name)
    merger.close()
    print("output location : ", os.getcwd()+"/"+name)

user_question = int(input("How many pdf you want to merge? : "))

for i in range(user_question):
    path = input("Enter the location with pdf file : ")
    check_file = os.path.isfile(path)
    if not check_file and not path.endswith(".PDF" or ".pdf"):
        print("Invalid Directory/File ❌. Please Enter The Valid Location With pdf file")
        exit()
    else:
        pass
    print("Selected file : ", path)
    pdf_store.append(path)

for j in pdf_store:
    merger.append(j)

user_ask = str(input("You Want to set name of the merged pdf y/n :"))

if user_ask == "y" or user_ask == "Y":
    name_pdf = str(input("Enter the name of the new PDF : "))
    if name_pdf.endswith(".pdf") or name_pdf.endswith(".PDF"):
        pdf_merger(name_pdf)
        print()
    else:
        print()
        pdf_merger(name_pdf+".pdf")
else:
    print()
    print("The pdf file saved Default name by : Merged.pdf")
    pdf_merger("Merged.pdf")
exit()