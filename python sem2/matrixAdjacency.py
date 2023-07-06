#Write a Program to check if a given graph is a complete graph. Represent the graph using adjacency matrix representation. 

import numpy as np

def is_complete_graph(adjacency_matrix):
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if i != j and adjacency_matrix[i][j] != 1:
                return False
    return True

adjacency_matrix = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

print("Is complete graph:", is_complete_graph(adjacency_matrix))

