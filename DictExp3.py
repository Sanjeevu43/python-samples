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
