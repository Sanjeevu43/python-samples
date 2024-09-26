'''
Before performing any operation on the file like reading or writing, first, we have to open that file. 
For this, we should use Python’s inbuilt function open() but at the time of opening, 
we have to specify the mode, which represents the purpose of the opening file. '''

# f = open(filename, mode)

'''
Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
'''
# Read
f = open('C:\PythonExps\Files\one.txt', 'r')

for each in f:
    #None
    print(each)
#print(f.read(3))
# Write
f1 = open('C:\\PythonExps\\Files\\four.txt', 'w')
f1.write("Head Good City")
f1.close()

# Append

f1 = open('C:\\PythonExps\\Files\\two.txt', 'a')
f1.write(" Tadipatri")
f1.close()

with open('C:\\PythonExps\\Files\\two.txt','w') as file:
    file.write('JMD')

#f1.write(" PDTR")