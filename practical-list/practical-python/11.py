# Write a function that prints a dictionary where the keys are numbers between 1 and 5
# and the values are cubes of the keys.

def cube_dict():
    cube_dict = {}
    for i in range(1, 6):
        num = int(input(f"Enter number {i}: "))
        cube_dict[i] = num ** 3
    print(cube_dict)
cube_dict()
