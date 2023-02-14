#Write a python program to solve the following 

#This program uses the numpy library to perform the matrix operations. The np.array function creates a numpy array, which is essentially a matrix in numpy. The np.transpose function is used to perform the transpose operation, and np.conj function is used to calculate the conjugate of the matrix. The .T operator is used to transpose the result of the conjugate operation, effectively giving us the conjugate transpose of the matrix.

import numpy as np

def main():
    # Create a vector
    vector = np.array([1, 2, 3])
    print("Vector:", vector)

    # Create a matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matrix:", matrix)

    # Transpose of a vector
    vector_transpose = np.transpose(vector)
    print("Transpose of the vector:", vector_transpose)

    # Transpose of a matrix
    matrix_transpose = np.transpose(matrix)
    print("Transpose of the matrix:", matrix_transpose)

    # Conjugate transpose of a vector
    vector_conjugate_transpose = np.conj(vector).T
    print("Conjugate transpose of the vector:", vector_conjugate_transpose)

    # Conjugate transpose of a matrix
    matrix_conjugate_transpose = np.conj(matrix).T
    print("Conjugate transpose of the matrix:", matrix_conjugate_transpose)

if __name__ == "__main__":
    main()
