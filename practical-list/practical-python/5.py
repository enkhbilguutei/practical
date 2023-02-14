# WAP to perform the following operations on a string
# a. Find the frequency of a character in a string.
# b. Replace a character by another character in a string.
# c. Remove the first occurrence of a character from a string.
# d. Remove all occurrences of a character from a string.

def char_frequency(s, c):
    """Finds the frequency of a character in a string"""
    return s.count(c)

def replace_char(s, old_c, new_c):
    """Replaces a character with another character in a string"""
    return s.replace(old_c, new_c)

def remove_first_char(s, c):
    """Removes the first occurrence of a character from a string"""
    return s.replace(c, '', 1)

def remove_all_chars(s, c):
    """Removes all occurrences of a character from a string"""
    return s.replace(c, '')

# Example usage
s = "hello world"
c = 'l'
print(f"Frequency of {c} in '{s}': {char_frequency(s, c)}")
print(f"Replacing {c} with 'X' in '{s}': {replace_char(s, c, 'X')}")
print(f"Removing first {c} from '{s}': {remove_first_char(s, c)}")
print(f"Removing all {c} from '{s}': {remove_all_chars(s, c)}")
