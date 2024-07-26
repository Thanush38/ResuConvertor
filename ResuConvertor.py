import os
import sys
from dotenv import load_dotenv
from docx2pdf import convert


def getName(data):
    load_dotenv()
    if(data=="-r"):
        resumeName = os.getenv("RESUME_NAME")
        return resumeName
    elif(data=="-c"):
        coverName = os.getenv("COVER_LETTER_NAME")
        return coverName
    elif (data=="-a"):
        resumeName = os.getenv("RESUME_NAME")
        coverName = os.getenv("COVER_LETTER_NAME")
        return resumeName, coverName
    else: 
        return "Invalid Argument"



def mainFunc():
    for i in sys.argv:
        if(i=="-r"):
            resumeName = getName(i)
            ConvertToPDF(resumeName)
        elif(i=="-c"):
            coverName = getName(i)
            ConvertToPDF(coverName)
        elif(i=="-a"):
            resumeName, coverName = getName(i)
            ConvertToPDF(resumeName)
            ConvertToPDF(coverName)
        else:
            print("Invalid Argument")


def ConvertToPDF(fileName):
    convert(fileName, fileName + ".pdf")
    
mainFunc()