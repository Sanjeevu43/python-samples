
#x = []
def f1(msg):
    x = []
    i = 20
    if i>20:
        print("OK1")
    else:
        x={}
        x[0]={'ID':1}

    print('X:',x)  
    return msg

message = f1("Welcome to Python World")
print(message)

x = 13//2
print('X=',x)
name = 'Sanjeev'
print(f'Hello {name}')

def getName(name) -> None:
    return f'Hello {name}'

res = getName(name)
print(res)

def getName1(name) -> None:
    return 'Hello {}'.format(name)

res = getName1(name)
print(res)

easyocr = 0
if easyocr is None:  # this condition is True if easyocr is None
    print('easyocr value is:', easyocr)

if easyocr: # this condition is True if easyocr has any +ve or -ve value, if is it 0 or None then False
     print('easyocr value is:', easyocr)
print(easyocr)
age = 34
if 15 < age < 35:
    print('Ok')

person = None
print(type(person))

age: int = 30
print('Age type :',type(age))
age = 'Sanjeev'
print('Age type :',type(age))

