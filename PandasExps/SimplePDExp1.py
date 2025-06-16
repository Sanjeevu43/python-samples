import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame({'Brand':['Maruthi','Tata','Hyundai','Mahindra','Renault','Ford','Tata','Maruthi'],
                    'Year':[2020,2021,2020,2019,2020,2018,2022,2021],
                    'KMS Driven':[10000,15000,9000,17000,11000,17000,13000,8000],
                    'City':['Bangalore','Hyderabad','Pune','Bangalore','Chennai','Delhi','Hyderabad','Bangalore'],
                    'Mileage':[19,19,18,17,17,17,18,18]

})
#print(data)
print('====================================================================')
print('====================================================================')

person1 = [['Sanjeev',45,'M','India'],
          ['Bindu',40,'F','India'],
          ['Lucky',15,'F','India'],
          ['Bittu',8,'F','India'],
          ['Smithi',6,'F','UK'],
          ['Umma',60,'F','India'],
          ['Munni',38,'F','UK'],
          ['Vinod',47,'M','UK'],
          ['Raghu',35,'M','UK']]

person = [['Sanjeev',45,'M','India'],
          ['Bindu',40,'F','India'],
          ['Lucky',15,'F','India'],
          ['Bittu',8,'F','India'],
          ['Smithi',6,'F','UK'],
          ['Umma',60,'F','India'],
          ['Munni',38],
          ['Vinod',47],
          ['Raghu',35]]

data2 = pd.DataFrame(person,columns=['Name','Age','Gender','Country'])
print(data2)
print('====================================================================')
print('====================================================================')

#print(data2.iloc[:,[0,1]].values) # gives all rows values for column 1 & 2 without column names
#print(data2.iloc[:,[0,1]]) # gives all rows values for column 1 & 2 with column names

print(data2.iloc[:3,[0,1]]) # iloc is used for split both rows and columns
print(data2[:3]) # valid line 
# print(data2[:3,[0,1]]) # invalid syntax # slicing is used for split only rows not columns

#print(data2['Name']) # gives only Name column values without column name
#print(data2.dtypes)

#print(data2.isnull().sum())# check the no of missing values in each column (gives count of missing values)

# Train and Test data
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
print(Y_test) '''