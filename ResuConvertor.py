import os
import sys
from dotenv import load_dotenv
from docx2pdf import convert
from pypdf import PdfWriter
from datetime import date
import shutil

load_dotenv()

company = input("What Company is this for: ")
position = input("What Position:")
name = os.getenv("NAME")

def getName(data):
    load_dotenv()
    if(data=="-r"):
        resumeName = os.getenv("RESUME_NAME")
        # docName.add(resumeName)
        return resumeName
    elif(data=="-c"):
        coverName = os.getenv("COVER_LETTER_NAME")
        # docName.add(coverName)
        return coverName
    elif (data=="-rc"):
        resumeName = os.getenv("RESUME_NAME") 
        coverName = os.getenv("COVER_LETTER_NAME")
        # docName.add(resumeName)
        # docName.add(coverName)
        return resumeName, coverName
    elif (data=="-rct"):
        resumeName = os.getenv("RESUME_NAME") 
        coverName = os.getenv("COVER_LETTER_NAME")
        transcript= os.getenv("TRANSCRIPT_NAME")
        return resumeName, coverName, transcript
    else: 
        return "Invalid Argument"



def mainFunc(data):
    if(data=="-r"):
        resumeName = getName(data)
        ConvertToPDF(resumeName)
        saveOldVersion([resumeName+".pdf"] )
    elif(data=="-c"):
        coverName = getName(data)
        ConvertToPDF(coverName)
        saveOldVersion([coverName+".pdf"] )
    elif(data=="-rc"):
        resumeName, coverName = getName(data)
        ConvertToPDF(resumeName)
        ConvertToPDF(coverName)
        saveOldVersion([resumeName+".pdf",coverName+".pdf"] )
    elif(data=="-rcc"):
        resumeName, coverName = getName("-rc")
        ConvertAndCombine(resumeName,coverName, null)
    elif(data=="-rctc"):
        resumeName, coverName, transcript = getName("-rct")
        ConvertAndCombine(resumeName,coverName, transcript)
    else:
        print("unvalid argument")
        


def ConvertToPDF(fileName):
    convert(fileName+".docx", fileName + ".pdf")

def ConvertAndCombine(resume, cover, transcript):
    convert(resume+".docx", resume + ".pdf")
    convert(cover+".docx", cover + ".pdf")
    merger = PdfWriter()
    merger.append(resume+ ".pdf")
    merger.append(cover+ ".pdf")
    if(transcript):
        merger.append(transcript+".pdf")
    newName = f"{name} {company} {position}.pdf"
    merger.write(newName)
    merger.close()
    os.remove(resume + ".pdf")
    os.remove(cover + ".pdf")
    saveOldVersion([newName] )

def saveOldVersion(files):
    if(not os.path.exists("./past")):
        os.makedirs("./past")
    
    folderName = getFolderName(company,position)
    os.makedirs("./past/" + folderName)
    for file in files:
        shutil.copyfile("./" + file, "./past/" + folderName+"/" + file)
        os.remove(file)
    

def getFolderName(company, position):
    folderName = company + "-" + position + " " + str(date.today())
    return folderName

    
mainFunc(sys.argv[1])