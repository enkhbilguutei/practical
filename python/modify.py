from CircleWithException import Circle 

try: 
    c1 = Circle(5)
    print("C1 with radius 5's area is", c1.getArea())
    c2 = Circle(-5)
    print("C2 with radius -5's area is", c2.getArea())
except ValueError: 
    print("Invalid radius, radius must be greater than 0")

try: 
    c3 = Circle(0)
    print("C3 with radius 0's area is", c3.getArea())
except ValueError: 
    print("Invalid radius, radius must be greater than 0")
