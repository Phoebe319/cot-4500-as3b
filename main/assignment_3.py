import numpy as np

def gaussian(matrix):
    holder = matrix[0].copy()
    matrix[0] = matrix[1].copy()
    matrix[1] = holder

    matrix[1] = matrix[1] - 2 * matrix[0]
    matrix[2] = matrix[2] + matrix[0]

    matrix[1] = matrix[1] / matrix[1][1]

    matrix[2] = matrix[2] - matrix[2][1] * matrix[1]

    z = matrix[2][3] / matrix[2][2]
    y = matrix[1][3] - matrix[1][2] * z
    x = matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z

    return x, y, z

def matrix_determinant(matrix):
    determinant = np.linalg.det(matrix)
    return determinant

def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

        L[i, i] = 1

    return L, U