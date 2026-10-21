import numpy as np


def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.

    if len(a[0]) != len(b):
        return -1

    a_array = np.array(a)
    b_array = np.array(b)

    return (a_array @ b_array).tolist()


if __name__ == "__main__":
    print(matrix_dot_vector([[1, 2], [2, 4]], [1, 2]))
