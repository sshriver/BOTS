from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import os
from pandas import *
import math
import sys

#For email functionality
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

#For secure password retrieval
import getpass

root = Tk()
root.geometry("500x300")

#strvars
varImportFile = StringVar()
varColumnNames = StringVar()
varFormatTypes = StringVar()
varImportError = StringVar()
varSaveError = StringVar()
varSaveError.set(" ")
varImportError.set("Please select a valid file type(CSV)")
varChecked = []
state = 0


dataList = None
data = None
#booleans
boolCsv = 0
list = NONE
x = 0


def openFile():
    fileName = askopenfilename()
    root.update()
    if (fileName == ""):
        fileName = "Please select a file"
    fileNameDisplay = os.path.basename(fileName)
    varImportFile.set(fileNameDisplay)
    print(fileNameDisplay[(len(fileNameDisplay)-4): (len(fileNameDisplay))])
    if(fileNameDisplay[(len(fileNameDisplay)-4): (len(fileNameDisplay))] != ".csv"):
        varImportError.set("Please select a valid file type(CSV)")
        boolCsv = 0
    else:
        global data
        try:
            clearOptionMenu()
        except:
            pass
        varImportError.set("File type accepted           ")
        df = read_csv(fileNameDisplay)
        omColumnMenu['menu'].delete(0)
        data = df
        global dataList
        global list
        dataList = df.values.tolist()
        list = [[0 for x in range(len(dataList[0]))]for y in range(len(dataList))]
        boolCsv = 1
        populateOptionMenu(dataList, data)
        populateList()
        return dataList

    #omColumnMenu['menu'].insert('end','command',label='bleh')
   

def rfrsh():
    varColumnNames.set(columnNames[0])
    omColumnMenu

def populateOptionMenu(dataList, data):
   
    #function to populate the option menu with check boxes from the 
    for i in range(len(dataList[0])):
        var = IntVar()
        varChecked.append(var)
        omColumnMenu['menu'].insert('end','checkbutton',variable=varChecked[i], label=data.columns[i])
    #varColumnNames.set(columnNames)

def clearOptionMenu():
    global varChecked
    print("------")
    for i in range (data.shape[1]):
        varChecked = []
        omColumnMenu['menu'].delete(0)
    
def test():
    #fp = filedialog.askdirectory()
    print(varFormatTypes.get())
    pwBox = Entry(frameBottom, show="*", width=15)
    pwBox.pack()
    print(len(varChecked))
    #for i in range(len(dataList[0])):       
     #  print(i, " : ", varChecked[i].get())
    #print(varColumnNames.get())
    #selectAll()

def populateList():
    #function to populate the list variable with values from CSV
    global list
    for i in range(len(dataList)):
        for x in range(len(dataList[i])):
            list[i][x] = str(dataList[i][x])
def formatData():
    returnFile()
    print(state)
    global list
    global x
    #try catch to see if you actually have a file
    try:
        for i in range(len(dataList)):
            for x in range(len(dataList[i])):
                p = dataList[i][x]
                #check to see if the column was selected
                #if column is selected to format
                if(varChecked[x].get() == 1):
                    if(state <3 ):
                        #state is less then 3 this means its formatting for a number.
                        #state 0 = rounding
                        #state 1 = C to F(temp)
                        #state 2 = F to C(temp)

                        try:
                            #check to see if the value is a number or not
                            p = float(p)
                            #if nan(not a number) pass
                            if(math.isnan(p)):
                                list[i][x] = str(0)
                                pass
                            else:
                                if(state == 0):                                   
                                    rounded = p
                                    #round to 1 decimal place
                                    rounded = round(rounded, 1)
                                    list[i][x] = str(rounded)
                                    #print(str(rounded))
                                
                                elif(state ==1):
                                    temp = p * (9/5) + 32
                                    list[i][x] = str(temp)
                                    pass
                                elif(state ==2):
                                    temp = (p - 32) * (5/9)
                                    list[i][x] = str(temp)
                                    pass
                                else:
                                    pass
                        except ValueError:
                            list[i][x] = p
                            pass
                        
                else:
                    pass
        x = len(list)
        varSaveError.set("File successfully formated")
    except:
        varImportError.set("Please select a valid file type(CSV) first")
    
def returnFile():
    global state
    if(varFormatTypes.get()== "        Round to 2 decimals      "):
        state = 0
    elif(varFormatTypes.get() == "Convert Celius to Fahrenheit"):
        state = 1
    elif(varFormatTypes.get() == "         Convert Fahrenheit       "):
        state = 2
        
def saveFile():
    global dataList
    if (dataList == None):
        varSaveError.set("No file selected")
        pass
    else:
    #add the list to a csv file called test
    
        try:
            varSaveError.set("File saved successfully")
            with open('test1.csv','w', encoding = 'utf8') as csvfile:
                for i in range(0, x):
                    for counter in range(0, len(list[i])):
                        csvfile.write(str(list[i][counter]))
                        #seperate entries by ,
                        csvfile.write(',')
                    #seperate
                    csvfile.write('\n')
                csvfile.close()
            emailClient()
        except:
            varSaveError.set("File name currently open please close before saving")
def selectAll():
    for i in range(len(dataList[0])):       
        varChecked[i].set(1)
    pass
def deselectAll():
    for i in range(len(dataList[0])):       
        varChecked[i].set(0)
    pass
columnNames = [
    "Columns"
    ]
formatTypes = [
    "        Round to 2 decimals      ",
    "Convert Celius to Fahrenheit",
    "Convert Fahrenheit to Celius"
    ]
varColumnNames.set(columnNames[0])
varFormatTypes.set(formatTypes[0])

#frames
topFrame = Frame(root)
topFrame.pack(side=TOP)

frameMiddle2 = Frame(root)
frameMiddle2.pack(side=TOP)

frameMiddle = Frame(root)
frameMiddle.pack(side=TOP)


frameBottom = Frame(root)
frameBottom.pack(side=TOP)
#buttons
btnImport = Button(topFrame, text = "import", command=openFile)
btnImport.pack(side = RIGHT)

btnTest = Button(frameBottom, text = "Save", command=saveFile)
btnTest.pack(side=TOP)

btnFormat = Button(frameMiddle, text = "Format", command=formatData)
btnFormat.pack(side=RIGHT)

btnFormat = Button(frameMiddle, text = "Select All", command=selectAll)
btnFormat.pack(side=LEFT,pady=50)

btnFormat = Button(frameMiddle, text = "Deselect All", command=deselectAll)
btnFormat.pack(side=LEFT)

#labels
lblImportFileName = Label(topFrame, textvariable=varImportFile)
lblImportFileName.pack(side=LEFT)

lblFileTypeError = Label(frameMiddle2, textvariable=varImportError)
lblFileTypeError.pack()

lblSaveFileName = Label(frameBottom, textvariable=varSaveError)
lblSaveFileName.pack(side=TOP)
#optionmenu

omColumnMenu = OptionMenu(frameMiddle, varColumnNames, *columnNames)
#omColumnMenu['menu'].add_command(label="Select all", command = selectAll)


omFormatMenu = OptionMenu(frameMiddle, varFormatTypes, *formatTypes)
omFormatMenu.pack(side=RIGHT)
omColumnMenu.pack(side=RIGHT)


#email the output file
def emailClient():
    shouldEmail = input("Would you like to email this file? (Y/N): ")
    if (shouldEmail == "Y" or shouldEmail == "y"):
        email = input("Enter your email address: ")
        password = getpass.getpass("Enter password: ")
        sendEmail = input("Enter target email address: ")
        subject = input("Enter email subject: ")
        message = input("Enter email message: ")
        file_location = os.path.join(sys.path[0], "test2.csv")
        
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = sendEmail
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, sendEmail, text)
    server.quit()
root.mainloop()
