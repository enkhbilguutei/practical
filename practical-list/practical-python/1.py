#WAP to find the roots of a quadratic equation kk 
import math

def quadratic_equation_roots(a, b, c):
    """Finds the roots of a quadratic equation ax^2 + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    elif discriminant == 0:
        return -b / (2*a), None  # One real root
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        return (-b + sqrt_discriminant) / (2*a), (-b - sqrt_discriminant) / (2*a)  # Two real roots

# Example usage
print(quadratic_equation_roots(1, 0, -4))  # Should print (2.0, -2.0)


#In this code, we define a function quadratic_equation_roots that takes three parameters, a, b, and c, representing the coefficients of the quadratic equation. The function then calculates the discriminant and determines the number and value(s) of the roots based on the discriminant's value. If the discriminant is negative, the function returns None to indicate that there are no real roots. If the discriminant is zero, the function returns one root and None. If the discriminant is positive, the function returns two roots.

#The function is designed to be clear and easy to read by using informative variable names, concise conditional statements, and docstring to document the function's purpose. The code also uses the built-in math module to calculate the square root of the discriminant.


