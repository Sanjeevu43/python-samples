class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y   

# Example usage:

p1 = Point(1, 2)
p2 = Point(1, 2)  # Same coordinates as p1
p3 = Point(3, 4)  # Different coordinates

print(p1==p2)
