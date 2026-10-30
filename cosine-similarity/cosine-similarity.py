import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dp = np.dot(a, b)
    aNorm = np.sqrt(np.dot(a, a))
    bNorm = np.sqrt(np.dot(b, b))
    if aNorm == 0 or bNorm == 0:
        return 0.0
    else: 
        return float(dp / (aNorm * bNorm))
    pass