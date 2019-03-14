from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import os
from pandas import *
import math

root = Tk()
root.geometry("500x300")

#strvars
varImportFile = StringVar()
varColumnNames = StringVar()
varImportError = StringVar()
varSaveError = StringVar()
varSaveError.set(" ")
varImportError.set("Please select a valid file type(CSV)")
varChecked = []

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
   

    for i in range(len(dataList[0])):
        var = IntVar()
        varChecked.append(var)
        omColumnMenu['menu'].insert('end','checkbutton',variable=varChecked[i], label=data.columns[i])
    #varColumnNames.set(columnNames)

def clearOptionMenu():
    for i in range (data.shape[1]):
        omColumnMenu['menu'].delete(0)
    
def test():
    fp = filedialog.askdirectory()
    print(fp)
    #for i in range(len(dataList[0])):       
     #  print(i, " : ", varChecked[i].get())
    #print(varColumnNames.get())
    #selectAll()

def populateList():
    global list
    for i in range(len(dataList)):
        for x in range(len(dataList[i])):
            list[i][x] = str(dataList[i][x])
def formatData():
    global list
    global x
    print(len(dataList[1]))
    for i in range(len(dataList)):
        for x in range(len(dataList[i])):
            p = dataList[i][x]
            #check to see if the column was selected
            if(varChecked[x].get() == 1):               
                try:
                    #check to see if the value is a number or not
                    p = float(p)
                    #if nan(not a number) pass
                    if(math.isnan(p)):
                        list[i][x] = str(0)
                        pass
                    else:
                        rounded = p
                        #round to 1 decimal place
                        rounded = round(rounded, 1)
                        list[i][x] = str(rounded)
                        #print(str(rounded))
                except ValueError:
                    list[i][x] = p
                    pass
            else:
                pass
    x = len(list)

def saveFile():
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
varColumnNames.set(columnNames[0])
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

btnTest = Button(frameBottom, text = "test", command=saveFile)
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

omColumnMenu.pack(side=RIGHT)

root.mainloop()


