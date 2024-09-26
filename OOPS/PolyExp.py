class Parrot:
    def fly(self):
        print('Parrot can fly')

    def swimm(self):
        print('Parrot can not swimm')

p = Parrot()

def can_fly(bird):
    bird.fly()
    bird.swimm()

can_fly(p)



