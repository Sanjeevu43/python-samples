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
print('='*100)

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
print('='*100)
# Case 3

try:
    x = 9
    x>10
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('Must execute block')
print('will this print?')

print('='*100)

# Case 4

try:
    x = 'G'
    x>10
finally:
    print('Must execute block')  # this will print

print('will this print?  No') # this won't print


