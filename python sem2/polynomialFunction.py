#Write a program to evaluate a polynomial function (For example store f(x) = 4n^2 + 2n + 9 in an array and for a given value of n, say n = 5, compute the value of(n)).


def evaluate_polynomial(polynomial, n):
    result = 0
    for i in range(len(polynomial)):
        result += polynomial[i] * (n ** i)
    return result

polynomial = [4, 2, 9]
n = 5
print("f({}) = {}".format(n, evaluate_polynomial(polynomial, n)))
