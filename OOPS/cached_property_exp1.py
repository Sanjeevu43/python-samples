from functools import cached_property

class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.__dict__

    @cached_property
    def find_area(self):
        print('9')
        return 3.14 * self.radius ** 2
      
obj = Circle(5)
print(obj.find_area) # calculate radious
print(obj.find_area) # doen't recalculate the radious, retrives from the cache
obj.radius = 6  # changing the base attribute doesn't invalidate the cache
print('obj.radius',obj.radius)
print(obj.find_area)  # doen't recalculate radious, retrives from the cache
obj1 = Circle(6)
print(obj1.find_area) # Now recalculate the radious
       