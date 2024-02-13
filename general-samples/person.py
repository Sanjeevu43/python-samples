from pydantic import BaseModel,EmailStr,validator

class Person(BaseModel):
    name: str
    age: int
    is_married: bool
    email: str
    phone_no: int

    @validator("age")
    def validate_age(agevalue):
        if agevalue <= 0:
            raise ValueError(f'Age value must be grater than 0 : {agevalue}')
        return agevalue


# person = Person(name='Sanjeev',age=40,is_married=True,email='abc@gmail.com',phone_no=1234567890)
# print(person)
# print(person.name)

person_data = {'name':'Sanjeev','age':40,'is_married':True,'email':'abc@gmail.com','phone_no':1234567890}
person = Person(**person_data) # un-packing dict
print(person)

person1 = Person(name='Sanjeev',age=-1,is_married=True,email='abc@gmail.com',phone_no=1234567890)
print(person1)
    
