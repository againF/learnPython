import numpy as np

def matrix_operations(matrix_a, matrix_b):
    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)
    
    # Matrix addition
    matrix_sum = matrix_b + matrix_a
    print("Matrix A + B:", matrix_sum)

    matrix_product = np.dot(matrix_a, matrix_b)
    print("Matrix A * B:", matrix_product)

    transpose_matrix_a = np.transpose(matrix_a)
    transpose_matrix_b = np.transpose(matrix_b)
    print("Transpose of Matrix A:", transpose_matrix_a)
    print("Transpose of Matrix B:", transpose_matrix_b)

    try:
        inverse_matrix_a = np.linalg.inv(matrix_a)
        inverse_matrix_b = np.linalg.inv(matrix_b)
        print("Inverse of Matrix A:", inverse_matrix_a)
        print("Inverse of Matrix B:", inverse_matrix_b)
    except np.linalg.LinAlgError:
        print("Cannot compute the inverse of a singular matrix")

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_operations(matrix_a, matrix_b)