import numpy as np 


def cosine_similarity(a,b):
    """return cosine similarity

    Args:
        a (dataframe): _description_
        b (dataframe): _description_

    Returns:
        float64: cosine similarity
    """
    nominator = np.dot(a,b)

    a_norm = np.linalg.norm(a) 
    b_norm = np.linalg.norm(b)
    
    denominator = a_norm * b_norm
    cosine_similarity = nominator / denominator
    
    return cosine_similarity

