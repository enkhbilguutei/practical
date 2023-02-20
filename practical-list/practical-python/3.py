# WAP to create a pyramid of the character ‘*’ and a reverse pyramid

def pyramid(n):
    """Creates a pyramid of * with n rows"""
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))

def reverse_pyramid(n):
    """Creates a reverse pyramid of * with n rows"""
    for i in range(n, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1))

# Example usage
n = 5
print("Pyramid:")
pyramid(n)
print("Reverse Pyramid:")
reverse_pyramid(n)


#Entered by user 
# Get user input for pyramid height
# height = int(input("Enter pyramid height: "))

# # Create pyramid
# for i in range(1, height+1):
#     print(" "*(height-i) + "*"*(2*i-1))

# # Create reverse pyramid
# for i in range(height, 0, -1):
#     print(" "*(height-i) + "*"*(2*i-1))
