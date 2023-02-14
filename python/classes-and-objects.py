import math 


class InvalidRadiusException(Exception):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(f"Invalid radius: {radius}")

class GeometricObject:
    def __init__(self):
        pass

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.setRadius(radius)
        

    def getRadius(self): 
        return self.__radius 
    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius 
        else: raise InvalidRadiusException(radius)
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getDiamter(self): 
        return 2 * self.__radius 
    
    def getPerimeter(self):
        return 2 * self.__radius * math.pi
    
    def getCircumference(self):
        return 2 * math.pi * self.__radius

    def printCircle(self):
        print(self.__str__(), "radius", self.__radius)

circle = Circle(5)
print("Radius:", circle.getRadius())
print("Area:", circle.getArea())
print("Diameter:", circle.getDiamter())
print("Perimeter:", circle.getPerimeter())
print("Circumference:", circle.getCircumference())
circle.printCircle()
