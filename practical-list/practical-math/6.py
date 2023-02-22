#Generate basis of column space, null space, row space and left null space of a matrix space 
import numpy as np

# Define the matrix
A = np.array([[1, 2, 3],
              [2, 5, 3],
              [1, 0, 8]])

# Column space
C = np.linalg.matrix_rank(A)
col_space_basis = A[:, :C]
col_space_basis = np.linalg.qr(col_space_basis)[0]
print("Basis of column space:", col_space_basis)

# Null space
null_space_basis = np.linalg.qr(A.T)[0][:, C:]
print("Basis of null space:", null_space_basis)

# Row space
row_space_basis = np.linalg.qr(A)[0][:C, :]
print("Basis of row space:", row_space_basis)

# Left null space
left_null_space_basis = np.linalg.qr(A.T)[0][:, :C]
left_null_space_basis = left_null_space_basis.T
print("Basis of left null space:", left_null_space_basis)


# In this code, we use the numpy.linalg.matrix_rank() function to find the rank of the matrix, which gives us the number of pivot columns or pivot rows. We then use the numpy.linalg.qr() function to compute the QR decomposition of the matrix. The Q matrix of the QR decomposition contains an orthonormal basis for the column space or row space, depending on whether we apply it to the original matrix or its transpose. The R matrix of the QR decomposition contains information about the linearly independent vectors in the null space or left null space.

# Note that the basis vectors returned by numpy.linalg.qr() are not necessarily normalized. We can normalize them by dividing each vector by its Euclidean norm to obtain an orthonormal basis.