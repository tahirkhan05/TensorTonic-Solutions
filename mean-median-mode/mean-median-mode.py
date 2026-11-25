from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x=sorted(np.asarray(x, dtype=float))
    avg=np.mean(x)
    med=np.median(x)
    counts = Counter(x)
    mode_value, frequency = counts.most_common(1)[0]

    return {"mean": float(avg), "median": float(med), "mode": float(mode_value)}