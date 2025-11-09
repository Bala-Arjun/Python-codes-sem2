import numpy as np
A = np.array([[2, 3], [3, 4]])
B = np.array([8, 11])
solution = np.linalg.solve(A, B)
print("Solution (x, y):", solution)
