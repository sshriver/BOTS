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
        #if nan(not a number pass
        if(math.isnan(p)):
            list.insert(0, str(0))
            print(0)
            pass
        else:
            rounded = p
            #round to 1 decimal place
            rounded = round(rounded, 1)
            list.insert(0, str(rounded))
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
        file.write(list[x-1-i].encode())
        file.write('\n'.encode())
        
            
        

