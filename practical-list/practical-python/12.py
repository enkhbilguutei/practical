# 6. Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
# a. Print half the values of the tuple in one line and the other half in the next line.
# b. Print another tuple whose values are even numbers in the given tuple.
# c. Concatenate a tuple t2=(11,13,15) with t1.
# d. Return maximum and minimum value from this tuple

# Define the tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values of the tuple in one line and the other half in the next line.
half = len(t1) // 2
print(t1[:half])
print(t1[half:])

# b. Print another tuple whose values are even numbers in the given tuple.
even_tup = tuple(num for num in t1 if num % 2 == 0)
print(even_tup)

# c. Concatenate a tuple t2=(11,13,15) with t1.
t2 = (11, 13, 15)
concatenated_tup = t1 + t2
print(concatenated_tup)

# d. Return maximum and minimum value from this tuple
max_val = max(t1)
min_val = min(t1)
print("Max value:", max_val)
print("Min value:", min_val)
