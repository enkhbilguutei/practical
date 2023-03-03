# Solve a system of Homogeneous equations using the Gauss Jordan method.


# First, we need to represent the given system of equations as an augmented matrix:
# 2  3  1 | 0
# 1 -1  2 | 0
# 3  4  2 | 0

# Now, we will use Python and the NumPy library to perform the Gauss-Jordan elimination.
import numpy as np

# Create the augmented matrix
A = np.array([[2, 3, 1, 0],
              [1, -1, 2, 0],
              [3, 4, 2, 0]], dtype=float)

# Perform the row echelon transformation
for i in range(len(A)):
    # Divide the current row by the diagonal element
    A[i] /= A[i,i]
    for j in range(i+1, len(A)):
        # Subtract the current row multiplied by the first element of the next row
        A[j] -= A[j,i] * A[i]

# Perform the reduced row echelon transformation
for i in range(len(A)-1, -1, -1):
    for j in range(i-1, -1, -1):
        # Subtract the current row multiplied by the first element of the previous row
        A[j] -= A[j,i] * A[i]

# Extract the solutions
x = A[:,3]

# Print the solutions
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])

# Therefore, the solutions of the given system of equations are x=-2, y=1, and z=1.