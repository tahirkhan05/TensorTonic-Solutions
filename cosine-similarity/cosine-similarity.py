import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a=np.array(a, dtype=float)
    b=np.array(b, dtype=float)
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom==0:
        return 0.0
    result = np.dot(a,b) / denom
    return float(result)