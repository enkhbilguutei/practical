#Write a program to accept a directed graph G and compute the in-degree and out-degree of each vertex. 

import numpy as np 

def compute_in_out_degrees(adjacency_matrix):
    in_degrees = np.sum(adjacency_matrix, axis=0)
    out_degrees = np.sum(adjacency_matrix, axis=1)
    return in_degrees, out_degrees

adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0] 
])

in_degrees, out_degrees = compute_in_out_degrees(adjacency_matrix)
print("In degrees:", in_degrees)
print("Out degrees:", out_degrees)

