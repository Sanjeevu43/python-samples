emp = {'ID_3': "Jim", 'ID_2': "Jack"}
test_name = ''
def one():
    emp['one'] = {'ID_3': "Jim", 'ID_2': "Jack", 'ID_4': "Jane", 'ID_1': "Jill",'ID_10': "July"}
    test_name = 'San'
    print(emp)
    print(test_name)
    two()

def two():
    print('*********************************************************************************************')
    print(emp)
    print(test_name)

one()


name = 'Sanjeevu'
print("My name is {}".format(name))
print(f"My name is: {name}")
print('#########################################################################################################')
print("My name is %s" %name)
