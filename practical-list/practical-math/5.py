import numpy as np

def gauss_jordan(A):
    n, m = A.shape
    AI = np.hstack([A, np.eye(n)])
    
    for i in range(n):
        pivot = np.argmax(np.abs(AI[i:, i])) + i
        AI[[i, pivot]] = AI[[pivot, i]]
        AI[i, :] /= AI[i, i]
        
        for j in range(n):
            if j != i:
                AI[j, :] -= AI[j, i] / AI[i, i] * AI[i, :]
    
    return AI[:, n:]
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
X = gauss_jordan(A)
print(X)

