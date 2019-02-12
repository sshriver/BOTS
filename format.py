import pandas
import math
colnames = ['Year'
            ,'Product line'
            ,'Product type'
            ,'Product'
            ,'Order method type'
            ,'Retailer country'
            ,'Revenue'
            ,'Planned revenue'
            ,'Product cost'
            ,'Quantity'
            ,'Unit cost'
            ,'Unit price'
            ,'Gross profit'
            ,'UnitSalePrice'
            ]
print(colnames[2])
data = pandas.read_csv('Book1.csv', names=colnames)
#column name is Unit Sale Price
unitPrice = data.UnitSalePrice
#iterate through every row in the unitPrice column
total = ''
list = []
for p in unitPrice:
    #check to see if the value is a number or not
    try:
        #cast the number to a float
        p = float(p)
        #if nan(not a number) pass
        if(math.isnan(p)):
            list.append(str(0))
            print(0)
            pass
        else:
            rounded = p
            #round to 1 decimal place
            rounded = round(rounded, 1)
            list.append(str(rounded))
            total +=str(rounded)
            print(str(rounded))
    except ValueError:
        pass
#print the list
print(list)
x = len(list)
format = ''
#add the list to a csv file called test
with open('test.csv','wb') as file:
    for i in range(0, x):
        print(i)
        file.write(list[i].encode())
        file.write('\n'.encode())
        
            
        

