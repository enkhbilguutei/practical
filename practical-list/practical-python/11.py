# Write a function that prints a dictionary where the keys are numbers between 1 and 5
# and the values are cubes of the keys.

def print_cube_dict():
    cube_dict = {}
    for num in range(1, 6):
        cube_dict[num] = num ** 3
    print(cube_dict)

print_cube_dict()   # output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
