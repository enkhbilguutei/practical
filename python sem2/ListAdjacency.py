#Write a program to check if a given graph is complete graph. Represent the graph using adjacency List representation. 

def is_complete_graph(adjacency_list):
    for i in range(len(adjacency_list)):
        for j in range(len(adjacency_list)):
            if i != j and j not in adjacency_list[i]:
                return False
    return True

adjacency_list = [
    [1, 2, 3],
    [0, 2, 3],
    [0, 1, 3],
    [0, 1, 2]
]

print("Is complete graph:", is_complete_graph(adjacency_list))

