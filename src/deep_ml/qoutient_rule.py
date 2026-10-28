# https://www.deep-ml.com/problems/312?returnTo=track:math-foundations:basics

import numpy as np


def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.

    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative

    Returns:
        The derivative value f'(x)
    """
    gx = np.polyval(g_coeffs, x)
    dg = np.polyval(np.polyder(g_coeffs), x)

    hx = np.polyval(h_coeffs, x)
    dh = np.polyval(np.polyder(h_coeffs), x)

    return float((dg * hx - dh * gx) / (hx**2))


g_coeffs = [1, 0, 1]
h_coeffs = [1, 2]
x = 2.0

coeffcients = [2, 3, 5]


g = np.poly1d([2, 3, 5])

if __name__ == "__main__":
    print(quotient_rule_derivative(g_coeffs, h_coeffs, x))
    print(g(2))
    print(g.deriv())
    print(g.deriv()(2))
