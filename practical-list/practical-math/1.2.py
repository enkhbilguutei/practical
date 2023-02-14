import numpy as np 


vector = np.array([1,2,3,4])
print(vector)


# vector_transposed = np.transpose(vector)
# print(vector_transposed)

matrix = np.array([[1, 2, 3, 5, 6, 4 ]])
print(matrix)

# matrix_transposed = matrix.T
# print(matrix_transposed)

# matrix_conj_transposed = np.conj(matrix).T
# print(matrix_conj_transposed)


matric_reshaped = matrix.reshape(2, -1)
print(matric_reshaped)


# import numpy as np 

# arr1 = np.array([1,2,3,5,6,4])
# l = len(arr1)
# print(l)
# print(arr1.reshape(2,-1))
# arr2=arr1.reshape(2,3)
# print(arr2)
# print(arr2.shape)
# print("Number of rows")
# print(arr2.shape[[0]])
# rows=arr2.shape[0]
# print("Number of colums")
# print(arr2.shape[1])
# cols=arr2.shape[1]
# print("rows", rows, "columns",cols)
# for  r in range(rows):
#     print("row", r, end=" ")
#     print(arr2[r])
#  #accessing element wise 
# print("element wise access of a matrix")
#     for r in range (rows):
#         for c in range(cols): 
#             print(arr2[r][c], end=" ")
#             print()