import numpy as np

def inverse(matrix):
    """
    Calculates the cofactors, determinant, adjoint, and inverse of a matrix.
    """
    det = np.linalg.det(matrix)
    if det == 0:
        return None, None, None, None
    
    adj = np.linalg.inv(matrix).T * det
    cofactors = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            sub_det = np.linalg.det(sub_matrix)
            cofactors[i, j] = (-1)**(i + j) * sub_det
    inverse = adj / det
    
    return cofactors, det, adj, inverse

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
cofactors, det, adj, inverse = inverse(matrix)

print("Cofactors: \n", cofactors)
print("Determinant: \n", det)
print("Adjoint: \n", adj)
print("Inverse: \n", inverse)


#This will calculate the cofactors, determinant, adjoint, and inverse of the matrix matrix, which is given by np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). The results are stored in the variables cofactors, det, adj, and inverse, respectively. The output will be displayed on the console.