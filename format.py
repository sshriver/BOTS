from pandas import *
import math

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
#add the list to a csv file called test
with open('OUTPUT.csv','w', encoding = 'utf8') as csvfile:
    for i in range(0, x):
        for counter in range(0, len(list[i])):
            csvfile.write(str(list[i][counter]))
            #seperate entries by ,
            csvfile.write(',')
        #seperate 
        csvfile.write('\n')