import numpy as np 
import sys

from embedding_common import new_semantic,orthogonal_dimensions,filter_pairs
from utils_stereo_POLAR import get_antonym_pairs,build_dimensions
from fun import cosine_similarity
    
if __name__ == "__main__":
    POLAR_competent_high = 'css_word_embedding/stereotype/antonmy/POLAR_competent_high.csv'
    POLAR_competent_low = 'css_word_embedding/stereotype/antonmy/POLAR_competent_low.csv'
    POLAR_warmth_high = 'css_word_embedding/stereotype/antonmy/POLAR_warmth_high.csv'
    POLAR_warmth_low = 'css_word_embedding/stereotype/antonmy/POLAR_warmth_low.csv'
    
    word_competent_high = get_antonym_pairs(POLAR_competent_high)
    word_competent_low = get_antonym_pairs(POLAR_competent_low)
    word_warmth_high = get_antonym_pairs(POLAR_warmth_high)
    word_warmth_low = get_antonym_pairs(POLAR_warmth_low)
    # print(word_competent_high,type(word_competent_high))

    dir_competent_h = build_dimensions(word_competent_high)
    dir_competent_l = build_dimensions(word_competent_low)
    dir_competent = dir_competent_h - dir_competent_l
    
    dir_warmth_h = build_dimensions(word_warmth_high)
    dir_warmth_l = build_dimensions(word_warmth_low)
    dir_warmth = dir_warmth_h - dir_warmth_l

    dims = np.vstack((dir_competent,dir_warmth))
    print(dims)

    cos_sim = cosine_similarity(dir_warmth,dir_competent)

    print(cos_sim)
    

    
    orthogonal_dims = orthogonal_dimensions(dims)
    project_w_c = new_semantic(orthogonal_dims)
    
    print("Finish")
    
    
    
    
    