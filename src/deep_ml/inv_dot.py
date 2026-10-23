import numpy as np

a = np.array([[2, 3], [1, 4]])
b = np.array([[1, 2], [2, 4]])

X = np.array(
    [
        [1, 0],
        [1, 1],
        [1, 2],
    ],
    dtype=float,
)
y = np.array([1, 2, 2], dtype=float)

w = np.linalg.inv(X.T @ X) @ X.T @ y

inverse_a = np.linalg.inv(a)
inverse_b = np.linalg.inv(b)


if __name__ == "__main__":
    # print(inverse_a)
    print(w)
    # print(a @ inverse_a)
