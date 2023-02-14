# WAP to accept a number ‘n’ and
# j. Check if ’n’is prime
# k. Generate all prime numbers till ‘n’
# l. Generate first ‘n’ prime numbers This program may be done using functions
import math

def is_prime(n):
    """Checks if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_till_n(n):
    """Generates a list of all prime numbers till n"""
    primes = [2] if n >= 2 else []
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)
    return primes

def generate_first_n_primes(n):
    """Generates a list of the first n prime numbers"""
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

# Accept user input
num = int(input("Enter a number: "))

# Check if num is prime
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Generate all prime numbers till num
primes_till_num = generate_primes_till_n(num)
print(f"All prime numbers till {num}: {primes_till_num}")

# Generate first n prime numbers
n = int(input("Enter the value of n: "))
first_n_primes = generate_first_n_primes(n)
print(f"First {n} prime numbers: {first_n_primes}")



# In this program, we have defined three functions:
# is_prime(n): This function takes a number 'n' as input and checks if it is a prime number or not. It returns True if 'n' is prime and False otherwise.
# generate_primes_till_n(n): This function takes a number 'n' as input and generates a list of all prime numbers till 'n'.
# generate_first_n_primes(n): This function takes a number 'n' as input and generates a list of the first 'n' prime numbers.
# We then accept user input for the number 'num' and the value of 'n'. We check if 'num' is prime using the is_prime function and print the result. We also generate all prime numbers till 'num' and print the list. Finally, we generate the first 'n' prime numbers and print the list.
# Note that we have used the math module to calculate the square root of a number in the is_prime function. This improves the performance of the function as we only need to check for divisors up to the square root of the number.