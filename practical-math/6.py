#Generate basis of column space, null space, row space and left null space of a matrix space 

import numpy as np

def basis_of_matrix_spaces(matrix):
    u, s, vh = np.linalg.svd(matrix)
    
    # column space basis
    column_space_basis = vh.T[:, :np.sum(s > 1e-12)]
    
    # null space basis
    null_space_basis = vh.T[:, np.sum(s > 1e-12):]
    
    # row space basis
    row_space_basis = u[:, :np.sum(s > 1e-12)].T
    
    # left null space basis
    left_null_space_basis = u[:, np.sum(s > 1e-12):]
    
    return column_space_basis, null_space_basis, row_space_basis, left_null_space_basis

#Note: The value 1e-12 is used as a tolerance threshold to determine the rank of the matrix. It can be adjusted as needed.