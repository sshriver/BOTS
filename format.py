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

df = read_csv('WMBARR_DATA.csv')
data = df
dataList = df.values.tolist()
#column name is Unit Sale Price

total = ''
#initialize a 2d array.
list = [[0 for x in range(len(dataList[0]))]for y in range(len(dataList))]

for i in range(len(dataList)):
    for x in range(len(dataList[i])):
        #check to see if the value is a number or not
        p = dataList[i][x]
        try:
            #cast the number to a float
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
                total +=str(rounded)
                #print(str(rounded))
        except ValueError:
            list[i][x] = p 
            pass
#print the list
x = len(list)
format = ''
#add the list to a csv file called output
with open('OUTPUT.csv','w', encoding = 'utf8') as csvfile:
    for i in range(0, x):
        for counter in range(0, len(list[i])):
            csvfile.write(str(list[i][counter]))
            #seperate entries by ,
            csvfile.write(',')
        #seperate 
        csvfile.write('\n')

#email the output file
shouldEmail = input("Would you like to email this file? (Y/N): ")
if (shouldEmail == "Y" or shouldEmail == "y"):
    email = input("Enter your email address: ")
    password = getpass.getpass("Enter password: ")
    sendEmail = input("Enter target email address: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")
    file_location = os.path.join(sys.path[0], "OUTPUT.csv")
    
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