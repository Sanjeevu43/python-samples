
with open('C:\\PythonExps\\Files\\two.txt','r') as file:
    print(file.read())

with open('C:\\PythonExps\\Files\\two.txt','r') as file:
    print(file.readline())

with open('C:\\PythonExps\\Files\\two.txt','r') as file:
    print(file.readlines())

with open('C:\\PythonExps\\Files\\two.txt','r') as file:
    data = file.readlines()
    for eachLine in data:
        word = eachLine.split()
        print(word)

# Read (deafult mode is 'r')
f = open('C:\PythonExps\Files\one.txt')

for each in f:
    #None
    print(each)

# best practice 
try:
    f1 = open('C:\PythonExps\Files\one.txt')
    for each in f1:
        print(each)
finally:
    f1.close()
