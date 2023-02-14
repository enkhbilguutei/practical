# WAP to create a list of the cubes of only the even integers appearing in the input list
# (may have elements of other types also) using the following:
# a. 'for' loop
# b. list comprehension

# Using a for loop
def even_int_cubes_for_loop(lst):
    result = []
    for item in lst:
        if isinstance(item, int) and item % 2 == 0:
            result.append(item ** 3)
    return result

# Using a list comprehension
def even_int_cubes_list_comprehension(lst):
    return [item ** 3 for item in lst if isinstance(item, int) and item % 2 == 0]

input_list = [1, 2, 3, 4, '5', 6, 7, 8.0]
even_int_cubes_for_loop_result = even_int_cubes_for_loop(input_list)
even_int_cubes_list_comprehension_result = even_int_cubes_list_comprehension(input_list)
print(f"Using for loop: {even_int_cubes_for_loop_result}")
print(f"Using list comprehension: {even_int_cubes_list_comprehension_result}")
