import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x=np.asarray(X, dtype=float)
    x_cov=x-np.mean(x, axis=0)
    xct=x_cov.T
    return np.matmul(xct,x_cov)/(x.shape[0] - 1)