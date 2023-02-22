# Solve a system of Homogeneous equations using the Gauss Jordan method.
# Function to perform Gauss-Jordan elimination
import numpy as np

# Define the coefficients of the homogeneous equations
A = np.array([[1, 2, 3],
              [2, 5, 3],
              [1, 0, 8]], dtype=float)

# Apply Gauss-Jordan elimination
n = len(A)
for i in range(n):
    # Find the pivot element
    pivot = A[i][i]
    # Divide the row by the pivot element to make it 1
    A[i] /= pivot
    # Subtract the pivot row from all other rows to make the elements below the pivot zero
    for j in range(n):
        if j != i:
            A[j] -= A[i] * A[j][i]

# Print the solution vector
x = np.zeros(n)
for i in range(n):
    x[i] = A[i][-1]
print("Solution vector:", x)

# 0x + 0y + 1z = 0
# 0x + 0y + 1z = 0
# 0x + 0y + 1z = 0


# The solution vector [0. 0. 1.] corresponds to a system of homogeneous equations. In general, a system of homogeneous linear equations has a non-trivial solution if and only if the determinant of the coefficient matrix is zero (i.e., the system is singular).

# To find the system of equations that corresponds to this solution vector, we can set up a matrix equation in the form Ax = 0, where A is the coefficient matrix and x is the solution vector. Since the solution vector is [0 0 1], this means that the third variable in the system has a coefficient of 1 and the other variables have a coefficient of 0 in each equation.

# For example, one possible system of homogeneous linear equations that corresponds to the solution vector [0 0 1] is: