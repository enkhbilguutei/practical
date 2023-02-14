# WAP to define a class Point with coordinates x and y as attributes. Create
# relevant methods and print the objects. Also define a method distance to calculate the
# distance between any two point objects
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# create two Point objects
p1 = Point(0, 0)
p2 = Point(3, 4)

# print the objects
print(p1)   # output: (0, 0)
print(p2)   # output: (3, 4)

# calculate the distance between the two points
distance = p1.distance(p2)
print(distance)   # output: 5.0

