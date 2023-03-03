# Find cofactors, determinant, adjoint and inverse of a matrix. 
import numpy as np

# Step 1: Define the matrix
A = np.array([[2, 3, -1],
              [4, -2, 5],
              [3, 1, 4]])

# Step 2: Define a function to calculate the determinant of a submatrix
def det(A):
    n = A.shape[0]
    if n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        d = 0
        for j in range(n):
            M = np.delete(np.delete(A, 0, axis=0), j, axis=1)
            d += ((-1)**j) * A[0][j] * det(M)
        return d

# Step 3: Define a function to calculate the cofactor of each element of the matrix
def cofactor(A):
    n = A.shape[0]
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            M = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i][j] = ((-1)**(i+j)) * det(M)
    return C

# Step 4: Define a function to calculate the adjoint of the matrix
def adjoint(A):
    C = cofactor(A)
    return C.transpose()

# Step 5: Define a function to calculate the inverse of the matrix
def inverse(A):
    d = det(A)
    if d == 0:
        print("Matrix is singular, cannot find inverse")
        return None
    else:
        adj = adjoint(A)
        return adj/d

# Print the matrix and its cofactors, determinant, adjoint, and inverse
print("Original matrix:")
print(A)
print("Cofactors:")
print(cofactor(A))
print("Determinant:")
print(det(A))
print("Adjoint:")
print(adjoint(A))
print("Inverse:")
print(inverse(A))


# In this code, we first ask the user to enter the size of the square matrix, and then the matrix elements row-wise. We use a nested loop to read the elements into a NumPy array called matrix.

# We then define four functions to find the determinant, cofactor matrix, adjoint matrix, and inverse matrix of a given matrix. The determinant function uses recursion to find the determinant of the matrix, by computing the determinants of smaller submatrices. The cofactor function uses nested loops to find the cofactor of each element of the matrix, by computing the determinants of smaller submatrices. The adjoint function uses the cofactor function to find the cofactor matrix, and then transposes it to get the adjoint matrix. The inverse function uses the determinant and adjoint functions to find the inverse matrix, by dividing the adjoint matrix by the determinant.

# We then print the original matrix, followed by the cofactor matrix, determinant, adjoint matrix, and inverse matrix, using the corresponding functions. If the determinant is zero, we print a message saying that the inverse does not exist.