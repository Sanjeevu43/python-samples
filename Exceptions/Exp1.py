# try:

# except:

# else:

# finally:

# Case 1
try:
    a = 10
    a = a/0
    print(a)
except Exception as ex:
    print('Caught Exception')
    print(ex)

finally:
    print('Finally block execute always')

print('This line will execute')

# Case 2

try:
    x = 'X'
    x>10
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('Must execute block')
print('will this print?')


