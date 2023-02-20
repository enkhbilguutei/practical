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
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Input two point objects from user
x1, y1 = map(int, input("Enter the coordinates of point 1 (separated by a space): ").split())
x2, y2 = map(int, input("Enter the coordinates of point 2 (separated by a space): ").split())
p1 = Point(x1, y1)
p2 = Point(x2, y2)

# Print the two point objects
print("Point 1:", p1)
print("Point 2:", p2)

# Calculate and print the distance between the two points
dist = p1.distance(p2)
print("Distance between the two points:", dist)

