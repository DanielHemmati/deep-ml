import numpy as np


def vector_sum(a: list[int | float], b: list[int | float]) -> list[int | float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    if len(a) != len(b):
        return -1

    return np.add(a, b).tolist()


a = [1, 3]
b = [4, 5]

if __name__ == "__main__":
    print(vector_sum(a, b))
