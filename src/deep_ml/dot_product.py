import numpy as np


def calculate_dot_product(vec1, vec2):
    return np.dot(vec1, vec2)


if __name__ == "__main__":
    print(calculate_dot_product([1, 2, 3], [4, 5, 6]))
