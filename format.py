from pandas import *
import math
import csv
colnames = ['Year'
            ,'Productline'
            ,'Producttype'
            ,'Product'
            ,'Ordermethodtype'
            ,'Retailercountry'
            ,'Revenue'
            ,'Plannedrevenue'
            ,'Productcost'
            ,'Quantity'
            ,'Unitcost'
            ,'Unitprice'
            ,'Grossprofit'
            ,'UnitSalePrice'
            ]
df = read_csv('Book1.csv', names=colnames)
data = df
dataList = df.values.tolist()
#column name is Unit Sale Price
#iterate through every row in the unitPrice column
total = ''
list = [[0 for x in range(len(colnames))]for y in range(len(dataList[0]))]

for i in range(len(colnames)):
    for x in range(len(dataList[i])):
        #check to see if the value is a number or not
        p = dataList[i][x]

        try:
            #cast the number to a float
            p = float(p)
            #if nan(not a number) pass
            if(math.isnan(p)):
                list[i][x] = str(0)
                print(0)
                pass
            else:
                rounded = p
                #round to 1 decimal place
                rounded = round(rounded, 1)
                #print(i)
                list[i][x] = str(rounded)
                total +=str(rounded)
                #print(str(rounded))
        except ValueError:
            list[i][x] = p 
            pass
#print the list
#print(list)
x = len(list)

format = ''
#add the list to a csv file called test

with open('test.csv','w', encoding = 'utf8') as csvfile:
    for i in range(0, x):
        print(list[i])
        for counter in range(0, len(list[i])):
            csvfile.write(list[i][counter])
            csvfile.write(',')
        csvfile.write('\n')
            
        

