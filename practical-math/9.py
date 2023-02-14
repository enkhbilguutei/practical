# Check the diagonalizable property of matrices and find the corresponding eigenvalue
# and verify the Cayley- Hamilton theorem

import numpy as np

# define the matrix A
A = np.array([[1, 2, 1], [6, -1, 0], [-1, -2, -1]])

# find the eigenvalues of A
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)

# check if A is diagonalizable
if len(eigenvectors) == A.shape[0]:
    print("A is diagonalizable.")
else:
    print("A is not diagonalizable.")

# verify the Cayley-Hamilton theorem
p = np.poly(A)
if np.allclose(np.dot(p, A), np.zeros_like(A)):
    print("The Cayley-Hamilton theorem is verified.")
else:
    print("The Cayley-Hamilton theorem is not verified.")


