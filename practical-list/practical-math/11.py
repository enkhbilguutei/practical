# Compute Gradient of a scalar field.

import numpy as np

# create a scalar field
scalar_field = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# compute the gradient of the scalar field
grad_x, grad_y = np.gradient(scalar_field)

# print the results
print("Gradient in x-direction:\n", grad_x)
print("Gradient in y-direction:\n", grad_y) 

