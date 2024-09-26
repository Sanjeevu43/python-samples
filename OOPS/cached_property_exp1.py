from functools import cached_property

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @cached_property
    def find_area(self):
        print('9')
        return 3.14 * self.radius ** 2

obj = Circle(5)
print(obj.find_area)
print(obj.find_area)