# Traditional way to construct or initialise values
# __init__ method will call automatically while Object creation
class Person:
    def __init__(self,name,age,id) -> None:
        self.name = name
        self.age = age
        self.id = id

    # magic function to return class object
    def __repr__(self):
        return ("Person (name={}, age={}, id={} )"
                .format(self.name, self.age, self.id))

person = Person('Sanjeev',40,101)
print(person.name)
print(person.age)
print(person.id)

# person object won't print if we don't ovrride __repr__ method
print(person) # O/T : Person (name=Sanjeev, age=40, id=101 )

# initialising values without __init__ method
# DataClasses provides a decorator and functions for automatically adding generated special methods 
# such as __init__() , __repr__() and __eq__() to user-defined classes.

from dataclasses import dataclass
from typing import List

@dataclass
class Person1():
    name: str = 'San'
    age: int = 30
    height: float = 1.90
    email: str = 'abc@gmail.com'

print(Person1())


@dataclass
class User:
    # Attributes Declaration
    # using Type Hints
    name: str
    age: int
    id: int
    email: str

user1 = User('Sanjeev',40,29,'abc@gmail.com')
print(user1)
user2 = User(name='Bindu',age=38,id=30,email='abc@gmail.com') # should get error but not
print(user2)

@dataclass
class People():
    people: List[User]

people = People([user1,user2])
print(people)
