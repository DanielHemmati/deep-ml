import numpy as np


def partial_pivoting_simpleVersion(A, row):
    max_row = np.argmax(np.abs(A[row:, row])) + row
    if max_row != row:
        A[[row, max_row]] = A[[max_row, row]]
    return A


def forward_elimination(A, row):
    for i in range(row + 1, len(A)):
        factor = A[i, row] / A[row, row]
        A[i, row:] -= factor * A[row, row:]
    return A


def backward_substituion(A, b):
    n = len(A)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[i, i]
    return x


def partial_pivoting(A_aug, row_num, col_num):
    # for i in range(row_num, rows):
    #     current_val = abs(A_aug[i, col_num])
    #
    #     if current_val > max_val:
    #         max_val = current_val
    #         max_row = i
    max_row = row_num + np.argmax(np.abs(A_aug[row_num:, col_num]))

    if max_row != row_num:
        A_aug[[row_num, max_row]] = A_aug[[max_row, row_num]]

    return A_aug


def gaussian_elimination(A, b):
    rows, cols = A.shape
    print(f"rows={rows}, cols={cols}")
    A_aug = np.hstack((A, b.reshape(-1, 1)))

    for i in range(rows - 1):
        A_aug = partial_pivoting(A_aug, i, i)
        for j in range(i + 1, rows):
            factor = A_aug[j, i] / A_aug[i, i]
            A_aug[j, i:] -= factor * A_aug[i, i:]

    x = np.zeros_like(b, dtype=float)
    for i in range(rows - 1, -1, -1):
        x[i] = (A_aug[i, -1] - np.dot(A_aug[i, i + 1 : cols], x[i + 1 :])) / A_aug[i, i]
    return x


A = np.array([[2, 8, 4], [2, 5, 1], [4, 10, -1]], dtype=float)
b = np.array([2, 5, 1], dtype=float)

if __name__ == "__main__":
    print(gaussian_elimination(A, b))
    # print(np.hstack((A, b.reshape(-1, 1))))
    # print(b.reshape(-1, 1))
