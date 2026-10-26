# url: https://www.deep-ml.com/problems/76?returnTo=track:math-foundations:basics
#
import numpy as np


def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
            vec1 (numpy.ndarray): 1D array representing the first vector.
            vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
            The cosine_similarity of the two vectors.
    """
    a = np.asarray(v1, dtype=float)
    b = np.asarray(v2, dtype=float)

    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine simi is undefined for zero vectors")

    return dot_product / (magnitude_a * magnitude_b)
