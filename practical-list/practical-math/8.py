# Find the orthonormal basis of a given vector space using the Gram-Schmidt
# orthogonalization process.

import numpy as np

def gram_schmidt_basis(vectors):
    basis = []
    for v in vectors:
        u = v - np.sum(np.dot(v, b)*b for b in basis)
        if not np.allclose(u, 0):
            e = u / np.linalg.norm(u)
            basis.append(e)
    return basis

vectors = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
basis = gram_schmidt_basis(vectors)
print(basis)
