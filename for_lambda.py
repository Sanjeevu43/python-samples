
names = ["San","Dan","Sam","Jhon","Nick","Tony","Ram"]

def get_names(name):
    return "Mr." + name

def test():
    if len(names) > 1:
        # dict comprehence
        name = {
            f"Name {n}" : get_names(names[n])
            for n in range(len(names))
              
        }
    print(type(name))
    print(name)

test()

for n in range(len(names)):
    pass
