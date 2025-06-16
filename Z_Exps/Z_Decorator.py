

def initialization(func):
    print(f'this is initialization function')
    func()

@initialization
def db_con():
    print(f'Establish DB connection')

db_con()