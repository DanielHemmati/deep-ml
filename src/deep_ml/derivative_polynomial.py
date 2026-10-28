import numpy as np


def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * x ** (n - 1)


if __name__ == "__main__":
    print(poly_term_derivative(2.0, 3.0, 2.0))
