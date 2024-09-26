from mimesis import Address,Person
from mimesis.locales import Locale
from mimesis.enums import Gender

person = Person(Locale.EN)
print(person.full_name(gender=Gender.FEMALE))
#print(person.full_name(gender=Gender.MALE))
print('---------------------------------------------------------------------------------')

en = Address(Locale.EN_GB)

#print(en.region())
print(en.country())
print(en.city())
print(en.street_name())
print(en.street_number())
print(en.address())
