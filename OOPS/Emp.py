class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        #print('Hai')
        print('Created Employee : {} - {}'.format(self.fullname,self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstname,self.lastname)

    
e1 = Employee('Sanjeevu','Penikalapati')
e2 = Employee('Hima','Penikalapati')

        