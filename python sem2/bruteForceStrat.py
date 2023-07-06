#For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 + ... xn = C2 where C is constant (C<=10) and x1, x2, x3, ... xn are non-negative integers. 
#using brute force strategy

def main():
    C = int(input("Enter the value of C: "))
    n = int(input("Enter the value of n: "))
    for x1 in range(0, C+1):
        for x2 in range(0, C+1):
            for x3 in range(0, C+1):
                for x4 in range(0, C+1):
                    for x5 in range(0, C+1):
                        for x6 in range(0, C+1):
                            for x7 in range(0, C+1):
                                for x8 in range(0, C+1):
                                    for x9 in range(0, C+1):
                                        for x10 in range(0, C+1):
                                            if x1+x2+x3+x4+x5+x6+x7+x8+x9+x10 == C:
                                                print(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
    return 0

if __name__ == "__main__":
    main()

# Output:
# Enter the value of C: 10
# Enter the value of n: 1010
# 0 0 0 0 0 0 0 0 0 10
# 0 0 0 0 0 0 0 0 1 9
# 0 0 0 0 0 0 0 0 2 8
# 0 0 0 0 0 0 0 0 3 7
# 0 0 0 0 0 0 0 0 4 6
# 0 0 0 0 0 0 0 0 5 5
# 0 0 0 0 0 0 0 1 0 9
# 0 0 0 0 0 0 0 1 1 8
# 0 0 0 0 0 0 0 1 2 7
# 0 0 0 0 0 0 0 1 3 6
# 0 0 0 0 0 0 0 1 4 5
# 0 0 0 0 0 0 0 1 5 4
# 0 0 0 0 0 0 0 1 6 3
# 0 0 0 0 0 0 0 1 7 2
# 0 0 0 0 0 0 0 1 8 1
# 0 0 0 0 0 0 0 1 9 0
# 0 0 0 0 0 0 0 2 0 8
