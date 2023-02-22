# Solve a system of Homogeneous and non-homogeneous equations using Gauss
# elimination method.
import numpy as np

# Define the coefficient matrix and the right-hand side vector
A = np.array([[2, 3, -4], [1, -1, 2], [3, 4, -1]])
b = np.array([0, 0, 8])

# Combine the coefficient matrix and the right-hand side vector into an augmented matrix
M = np.column_stack((A, b)).astype(np.cfloat)

# Perform row operations to transform the matrix into row echelon form
for i in range(len(M)):
    # Find the row with the largest absolute value in the ith column
    max_row = i
    for j in range(i + 1, len(M)):
        if abs(M[j, i]) > abs(M[max_row, i]):
            max_row = j
    
    # Swap the ith row with the row with the largest absolute value in the ith column
    M[[i, max_row]] = M[[max_row, i]]
    
    # Subtract a multiple of the ith row from all rows below it to eliminate the ith column
    for j in range(i + 1, len(M)):
        factor = M[j, i] / M[i, i]
        M[j] -= factor * M[i]

# Back-substitute to find the values of x, y, and z
x = np.zeros(3)
for i in range(len(M) - 1, -1, -1):
    x[i] = (M[i, -1] - np.dot(M[i, :-1], x)) / M[i, i]

print(x)


# Suppose we have the following system of equations:

# 2x + 3y - 4z = 0
# x - y + 2z = 0
# 3x + 4y - z = 8

# We can represent this system of equations in matrix form as follows:

# [2  3 -4 | 0]
# [1 -1  2 | 0]
# [3  4 -1 | 8]

# So the solution to the system of equations is x = -1, y = 2, and z = -1.

# Note that in this example, the first two equations are homogeneous (i.e., the right-hand side is zero), and the third equation is non-homogeneous (i.e., the right-hand side is 8). The Gauss elimination method works for both types of equations.



# import sys
# import numpy as np
# n=int(input("Enter number of variables: "))
# a=np.zeros((n,(n+1)))
# x=np.zeros(n)
# print('Enter coefficients of augmented matrix: ')
# for i in range(n):
#     for j in range(n+1):
#         a[i,j]=float(input('a['+str(i)+','+str(j)+']='))

# for i in range(n):
#     if a[i,i]==0.0:
#         sys.exit('Division by zero! ')
#     for j in range(i+1,n):
#         ratio=a[j,i]/a[i,i]
#         for k in range(n+1):
#             a[j,k]=a[j,k]- ratio*a[i,k]
# print('\nMatrix after forward phase:\n',a)

# x[n-1]=a[n-1,n]/a[n-1,n-1]
# for i in range(n-2,-1,-1):
#     x[i]=a[i,n]
#     for j in range(i+1,n):
#         x[i]=x[i]-a[i,j]*x[j]
#     x[i]=x[i]/a[i,i]

# print('\nSolution: ')
# for i in range(n):
#     print('X%d = %0.2f'%(i,x[i]))

# The first line prompts the user to enter the number of variables in the system of equations, and creates a numpy array of zeros with dimensions (n, n+1), where n is the number of variables. The extra column is for the right-hand side of the equations.

# The user is then prompted to enter the coefficients of the augmented matrix (i.e., the coefficients of the variables and the constants on the right-hand side).

# The code then performs the forward phase of Gaussian elimination with partial pivoting. In this phase, the code checks if the pivot element is zero, and if so, exits the program to avoid division by zero errors. Otherwise, the code calculates the ratios of the elements below the pivot to the pivot element and subtracts the appropriate multiple of the pivot row from each row below it to eliminate the element below the pivot. The result is an upper triangular matrix.

# The code then performs the back substitution phase to solve for the variables. It starts with the last equation (i.e., the one with the highest index), calculates the solution for the last variable (i.e., x_n), and then uses that solution to calculate the solution for the second-last variable (i.e., x_n-1), and so on until it has calculated the solution for all variables.

# Finally, the code prints the solution to the system of equations in the form "Xn = x, Xn-1 = y, ..., X1 = z", where n is the highest index of the variables.