# Compute Divergence of a vector field. 

import numpy as np

# Define the vector field represented by arrays u and v
u = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Compute the x and y gradients of the vector field
grad_x, grad_y = np.gradient(u, v)

# Compute the divergence of the vector field
div = grad_x + grad_y

print(div)
