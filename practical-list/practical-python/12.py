# 6. Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
# a. Print half the values of the tuple in one line and the other half in the next line.
# b. Print another tuple whose values are even numbers in the given tuple.
# c. Concatenate a tuple t2=(11,13,15) with t1.
# d. Return maximum and minimum value from this tuple

# Input the tuple from user
t1 = tuple(map(int, input("Enter the tuple t1: ").split()))

# Print half the values of the tuple in one line and the other half in the next line
n = len(t1)
mid = n // 2
print(t1[:mid])
print(t1[mid:])

# Print another tuple whose values are even numbers in the given tuple
t2 = tuple(filter(lambda x: x%2 == 0, t1))
print(t2)

# Concatenate a tuple t2=(11,13,15) with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print(t3)

# Return maximum and minimum value from this tuple
max_val = max(t3)
min_val = min(t3)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
