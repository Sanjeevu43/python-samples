class User:
    def __init__(self,name,email) -> None:
        self.name=name
        self.email=email

    def getUserInfo(self):
        print("Hi from", self)

    def __str__(self):
        #pass
       return (self.name + " ****** "+self.email)

users = [User('Sanjeevu','abc@gmail.com'),User('Lucky','Lucky@gmail.com')]

for user in users:
    user.getUserInfo()
    print(id(user))


x = 123456

print(str(x))





       