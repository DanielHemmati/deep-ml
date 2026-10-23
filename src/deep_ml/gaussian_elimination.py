import numpy as np


def partial_pivoting(A, row):
    max_row = np.argmax(np.abs(A[row:, row])) + row
    if max_row != row:
        A[[row, max_row]] = A[[max_row, row]]
    return A


def forward_elimination(A, row):
    for i in range(row + 1, len(A)):
        factor = A[i, row] / A[row, row]
        # NOTE: can you explain why row: ??
        A[i, row:] -= factor * A[row, row:]
    return A


# A = np.array([[2, 8, 4], [2, 5, 1], [4, 10, -1]], dtype=float)
# B = [[2, 8, 4], [2, 5, 1], [4, 10, -1]]

# A = np.array([[4, 10, -1], [0.0, 0.5, 1.5], [0, 0, 2]], dtype=float)
# b = np.array([2, 5, 1], dtype=float)
# x = np.zeros(3)
#
# Solve the last equation
# x[2] = b[2] / A[2, 2]
#
# Solve the second equation
# x[1] = (b[1] - A[1, 2] * x[2]) / A[1, 1]

# Solve the first equation
# x[0] = (b[0] - A[0, 1] * x[1] - A[0, 2] * x[2]) / A[0, 0]

if __name__ == "__main__":
    # print(partial_pivoting(A, 0))
    # print(forward_elimination(A, 0))
    print(x)
