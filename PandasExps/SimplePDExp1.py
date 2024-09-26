import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({'Brand':['Maruthi','Tata','Hyundai','Mahindra','Renault','Ford','Tata','Maruthi'],
                    'Year':[2020,2021,2020,2019,2020,2018,2022,2021],
                    'KMS Driven':[10000,15000,9000,17000,11000,17000,13000,8000],
                    'City':['Bangalore','Hyderabad','Pune','Bangalore','Chennai','Delhi','Hyderabad','Bangalore'],
                    'Mileage':[19,19,18,17,17,17,18,18]

})
print(data)
print('====================================================================')
print('====================================================================')

person = [['Sanjeev',45,'M','India'],
          ['Bindu',40,'F','India'],
          ['Lucky',15,'F','India'],
          ['Bittu',8,'F','India'],
          ['Smithi',6,'F','UK'],
          ['Umma',60,'F','India'],
          ['Munni',38,'F','UK'],
          ['Vinod',47,'M','UK'],
          ['Raghu',35,'M','UK']]

data2 = pd.DataFrame(person,columns=['Name','Age','Gender','Country'])
print(data2)
print('====================================================================')
print('====================================================================')
# values gives only row data 
# without values, it gives column names and row data
'''
print(data2.iloc[:,[0,1]].values) 
print(data2.iloc[:,[0,1]]) 

print(data2['Name']) # gives only Name column values without column name
print(data2.dtypes)
'''

X = data2.iloc[:,[0,1]]
Y = data2.iloc[:,[3]]
print('X Data : ',X)
print('Y Data : ',Y)
print('====================================================================')
print('====================================================================')
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)
print('====================================================================')
print(X_train)
print(X_test)
print('====================================================================')
print(Y_train)
print(Y_test)