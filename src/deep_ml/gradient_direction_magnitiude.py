# https://www.deep-ml.com/problems/308?returnTo=track:math-foundations:basics

import re

import numpy as np


def gradient_direction_magnitude(gradient: list) -> dict:
    gradient = np.asarray(gradient, dtype=float)

    magnitude = np.linalg.norm(gradient)

    if magnitude == 0:
        direction = np.zeros_like(gradient)
    else:
        direction = gradient / magnitude

    return {
        "magnitude": float(magnitude),
        "direction": direction.tolist(),
        "descent_direction": (-direction).tolist(),
    }


def gradient(x):
    # f(x,y) = x ** 2 + y ** 2
    return 2 * x


def gradient_info(x):
    g = gradient(x)

    # L2 norm
    magnitude = np.linalg.norm(g)

    # handle zero gradient
    if magnitude == 0:
        return magnitude, np.zeros_like(g)

    direction = g / magnitude

    return magnitude, direction


gradient_t = [3.0, 4.0]
# x = np.array([3.0, 4.0])

# magnitude, direction = gradient_info(x)

if __name__ == "__main__":
    print(gradient_direction_magnitude(gradient_t))
    # print("gradient:", gradient(x))
    # print("magnitude:", magnitude)
    # print("Direction:", direction)
    # print("descent direction:", -direction)
