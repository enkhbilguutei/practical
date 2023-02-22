#Generate the matrix into echelon form and find its rank. 
import numpy as np

# Define the matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]], dtype=float)

# Perform Gaussian elimination to transform matrix to echelon form
pivots = 0
for j in range(matrix.shape[1]):
    pivot_found = False
    for i in range(pivots, matrix.shape[0]):
        if matrix[i][j] != 0:
            matrix[[i, pivots]] = matrix[[pivots, i]]
            pivot_found = True
            break
    if pivot_found:
        for i in range(pivots+1, matrix.shape[0]):
            factor = matrix[i][j] / matrix[pivots][j]
            matrix[i] -= factor * matrix[pivots]
        pivots += 1

# Calculate rank of matrix based on number of pivot elements
rank = pivots
print("Matrix in echelon form:")
print(matrix)
print("Rank of matrix:", rank)
