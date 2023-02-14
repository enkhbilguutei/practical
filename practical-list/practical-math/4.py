# Solve a system of Homogeneous and non-homogeneous equations using Gauss
# elimination method.

import numpy as np

def gauss_elimination(A, b):
    """
    Solve a system of linear equations using the Gaussian elimination method
    
    Parameters:
        A (np.array): coefficient matrix of the system of linear equations
        b (np.array): right-hand side vector of the system of linear equations
    
    Returns:
        np.array: solution vector x of the system of linear equations Ax = b
    """
    # Augmented matrix [A|b]
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    n = A.shape[0]
    
    # Gaussian elimination
    for i in range(n):
        # Find the maximum value and its index in the current column (below the pivot)
        pivot = np.argmax(np.abs(Ab[i:, i])) + i
        # Swap the row containing the pivot with the current row
        Ab[[i, pivot]] = Ab[[pivot, i]]
        
        # Elimination
        for j in range(i+1, n):
            m = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= m * Ab[i, i:]
            Ab[j, -1] -= m * Ab[i, -1]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:-1], x[i+1:])) / Ab[i, i]
    
    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])
x = gauss_elimination(A, b)
print(x)
# Output: [2.0, 3.0, -1.0]
