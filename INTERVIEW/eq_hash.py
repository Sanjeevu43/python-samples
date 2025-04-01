class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Define equality: Two points are equal if their x and y coordinates are the same
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False  # Not equal if not a Point object

    def __hash__(self):
        # A simple hash function:  Combine the x and y coordinates to get a unique hash
        # Important:  If two objects are equal according to __eq__, they *must* have the same hash value.
        return hash((self.x, self.y))  # Using a tuple to hash multiple values is common

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage:

p1 = Point(1, 2)
p2 = Point(1, 2)  # Same coordinates as p1
p3 = Point(3, 4)  # Different coordinates

# print(id(p1))
# print(id(p2))
# print(id(p3))

print(p1 == p2)   # Output: True  (because their x and y coordinates are the same)
print(p1 == p3)   # Output: False

# print(hash(p1))   # Output: An integer (the hash value of p1)
# print(hash(p2))   # Output: Same integer as hash(p1) because p1 == p2
# print(hash(p3))   # Output: A different integer because p3 is different

# # Using the Point class as keys in a dictionary and in a set:

# my_dict = {p1: "Value for p1"}  # p1 is used as a key
# print(my_dict[p2])              # Output: Value for p1  (because p2 == p1, they have the same hash)

# my_set = {p1, p2, p3}  #  p1 and p2 are considered the same element, so the set contains only p1 and p3.
# print(my_set) # Output: {Point(1, 2), Point(3, 4)}