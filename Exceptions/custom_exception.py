
class InvalidAge(Exception):
    pass

age = int(input('Please enter age of the person:  '))

try:
    if age > 18 and age < 70:
        print('Valid Age')
    else:
        raise InvalidAge
except InvalidAge:
    print('Age should B/W 18 and 70')
finally:
    print('Execute always....')

 