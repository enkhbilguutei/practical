#Write a python program that generates all the permulations of a given set of digits with or without repetition.

import itertools

def generate_permutations(digits, repeat=False):
    permutations = []

    if repeat:
        # Permutations with repetition
        for r in range(1, len(digits) + 1):
            permutations.extend(itertools.product(digits, repeat=r))
    else:
        # Permutations without repetition
        permutations = list(itertools.permutations(digits))

    return permutations

digits = [1, 2, 3]
with_repetition = generate_permutations(digits, repeat=True)
without_repetition = generate_permutations(digits, repeat=False)

print("Permutations with repetition:")
for permutation in with_repetition:
    print(permutation)

print("\nPermutations without repetition:")
for permutation in without_repetition:
    print(permutation)

