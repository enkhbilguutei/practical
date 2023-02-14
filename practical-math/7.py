#Check the linear dependence of vectors. Generate a linear combination of given vectors
#of Rn/ matrices of the same size and find the transition matrix of given matrix space.
import numpy as np

def linear_dependence_and_combination(vectors):
    rank = np.linalg.matrix_rank(vectors)
    if rank < vectors.shape[0]:
        print("The vectors are linearly dependent.")
    else:
        print("The vectors are linearly independent.")
        
    # generate a linear combination of the vectors
    weights = np.random.rand(vectors.shape[1])
    linear_combination = np.dot(vectors, weights)
    
    return linear_combination

# import numpy as np

# def transition_matrix(matrix_a, matrix_b):
#     u, s, vh = np.linalg.svd(matrix_a)
#     u_prime, s_prime, vh_prime = np.linalg.svd(matrix_b)
    
#     # find the transition matrix
#     transition = np.dot(u_prime, np.dot(u.T, vh_prime))
    
#     return transition
