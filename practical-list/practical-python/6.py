#WAP to swap the first n characters of two strings

# def swap_first_n_chars(s1, s2, n):
#     """Swaps the first n characters of two strings"""
#     new_s1 = s2[:n] + s1[n:]
#     new_s2 = s1[:n] + s2[n:]
#     return new_s1, new_s2

# # Example usage
# s1 = "hello"
# s2 = "world"
# n = 3
# new_s1, new_s2 = swap_first_n_chars(s1, s2, n)
# print(f"Swapping the first {n} characters of '{s1}' and '{s2}': '{new_s1}', '{new_s2}'")




# Get input strings and n from user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
n = int(input("Enter value of n: "))

# Swap first n characters of the strings
new_string1 = string2[:n] + string1[n:]
new_string2 = string1[:n] + string2[n:]

# Print the swapped strings
print("Swapped strings are:")
print(new_string1)
print(new_string2)
