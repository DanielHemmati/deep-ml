import numpy as np

# url: https://www.deep-ml.com/problems/328?returnTo=track:math-foundations:basics


def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == "l1":
        return float(np.sum(np.abs(arr)))

    if norm_type == "l2":
        return float(np.sqrt(np.sum(np.square(arr))))

    if norm_type == "linf":
        return float(np.max(np.abs(arr)))

    if norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("Forbidden norm requires a 2D array")
        return float(np.sqrt(np.sum(np.square(arr))))

    raise ValueError(f"Invalid norm type: {norm_type}")


arr = np.array([[1, 2], [3, 4]])
norm_type = "l2"
# norm_type = "frobenius"

if __name__ == "__main__":
    print(compute_norm(arr, norm_type))
