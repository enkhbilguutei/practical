# Write a function that accepts two strings and returns the indices of all the occurrences
# of the second string in the first string as a list. If the second string is not present in the
# first string then it should return -1.

def find_all_occurrences(s1, s2):
    """Returns a list of indices of all occurrences of s2 in s1, or -1 if s2 is not present in s1"""
    indices = []
    start = 0
    while True:
        index = s1.find(s2, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    if not indices:
        return -1
    else:
        return indices

s1 = "hello world, world is awesome"
s2 = "world"
indices = find_all_occurrences(s1, s2)
print(f"The indices of '{s2}' in '{s1}' are: {indices}")
