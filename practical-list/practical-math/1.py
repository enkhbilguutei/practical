# Create and transform vectors and matrices (the transpose vector (matrix) conjugate
# transpose of a vector (matrix))

import numpy as np

# create a vector
vector = np.array(input("Enter a vector (separated by spaces): ").split(), dtype=np.float64)


rows, cols = map(int, input("Enter the dimensions of the matrix (separated by a space): ").split())
matrix = np.zeros((rows, cols), dtype=np.complex128)
for i in range(rows):
    row_input = input(f"Enter row {i+1} of the matrix (separated by spaces): ")
    row = np.array(row_input.split(), dtype=np.complex128)
    matrix[i, :] = row

# perform transformations
transpose_vector = vector.T
conjugate_transpose_vector = vector.conj().T
transpose_matrix = matrix.T
conjugate_transpose_matrix = matrix.conj().T

# print the results
print("Vector:", vector)
print("Transpose of vector:", transpose_vector)
print("Conjugate transpose of vector:", conjugate_transpose_vector)
print("Matrix:\n", matrix)
print("Transpose of matrix:\n", transpose_matrix)
print("Conjugate transpose of matrix:\n", conjugate_transpose_matrix)


# In this code, we use the NumPy library to create and manipulate vectors and matrices. We ask the user to input the elements of the vector and matrix, and we use NumPy's array function to convert the input strings into arrays with the appropriate data types (np.float64 for the vector, and np.complex128 for the matrix, since the user may input complex numbers).

# To create the matrix, we use a loop to input each row of the matrix separately, and then use NumPy's indexing syntax to assign each row to the appropriate row of the matrix.

# We then use NumPy's T attribute to compute the transpose of the vector and matrix, and the conj method to compute the conjugate of the matrix elements. Finally, we print the original and transformed vectors and matrices.