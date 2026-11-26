import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    x=np.asarray(X, dtype=float)
    n = x.shape[0]
    centered = x - np.mean(x, axis=0)
    covariance = (centered.T @ centered) / (n - 1)
    std = np.sqrt(np.diag(covariance))
    denom = np.outer(std, std)
    return covariance / denom