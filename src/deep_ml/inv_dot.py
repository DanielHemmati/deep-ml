import numpy as np

a = np.array([[2, 3], [1, 4]])

inverse = np.linalg.inv(a)


if __name__ == "__main__":
    print(inverse)
    print(a @ inverse)
