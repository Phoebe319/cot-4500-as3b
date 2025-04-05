from main.assignment_3 import gaussian, matrix_determinant, lu_decomposition
import numpy as np

augmented_matrix = np.array([[2, -1, 1, 6],
                              [1, 3, 1, 0],
                              [-1, 5, 4, -3]], dtype=float)

matrix = np.array([[1, 1, 0, 3],
                   [2, 1, -1, 1],
                   [3, -1, -1, 2],
                   [-1, 2, 3, -1]])

solution = gaussian(augmented_matrix)
rounded_solution = [round(val) for val in solution]
print(f"[{' '.join(map(str, rounded_solution))}]\n")

determinant = matrix_determinant(matrix)
print(determinant)

L, U = lu_decomposition(matrix)

print("\n", L)
print("\n", U)

'''
Question 3:
|9| >= |0| + |5| + |2| + |1| = 8 (true)
|9| >= |3| + |1| + |2| + |1| = 7 (true)
|7| >= |0| + |1| + |2| + |3| = 6 (true)
|12| >= |4| + |2| + |3| + |2| = 11 (true)
|8| >= |3| + |2| + |4| + |0| = 9 (false)
False

Question 4:
Matrix is symmetrical? Yes
(x^T)Ax > 0? Yes
True
'''
print("\nFalse\n")
print("True\n")