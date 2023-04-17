import numpy as np 
import sys

from embedding_common import new_semantic,orthogonal_dimensions,filter_pairs
from utils_stereo import get_antonym_pairs,build_dimensions
from fun import cosine_similarity
    
if __name__ == "__main__":
    
    ##### building pairs #####
    warmth_path = 'css_word_embedding/stereotype/antonmy/SCM_warmth_paris.csv'
    competent_path = 'css_word_embedding/stereotype/antonmy/SCM_competent_pairs.csv'
    # evaluation_path ='css_word_embedding/stereotype/antonmy/SD_evaluation_pairs.csv' # ingore it
    # potency_path = 'css_word_embedding/stereotype/antonmy/SD_potency_pairs.csv' # ingore it
    

    ant_pairs_warmth = get_antonym_pairs(warmth_path)
    ant_pairs_competent = get_antonym_pairs(competent_path)
    # ant_pairs_evaluation = get_antonym_pairs(evaluation_path) # ingore it
    # ant_pairs_potency = get_antonym_pairs(potency_path) # ingore it
    
    warm_pair = filter_pairs(ant_pairs_warmth)
    competent_pair = filter_pairs(ant_pairs_competent)
    # evaluation_pair = filter_pairs(ant_pairs_evaluation)  # ingore it
    # potency_pair = filter_pairs(ant_pairs_potency)  # ingore it
    
    
    ##### Get warmth and competent dimensions #####
    dir_warmth = build_dimensions(warm_pair)
    dir_competent = build_dimensions(competent_pair)
    # dir_evaluation = build_dimensions(evaluation_pair)  # ingore it
    # dir_potency = build_dimensions(potency_pair) # ingore it
    
    print(dir_warmth,dir_competent)

    cos_sim = cosine_similarity(dir_warmth,dir_competent)
    # cos_sim = cosine_similarity(dir_evaluation,dir_potency) # ingore it
    # print(cos_sim)
    
    dims = np.vstack((dir_warmth,dir_competent))
    # dims = np.vstack((dir_evaluation,dir_potency)) # ingore it
    
    orthogonal_dims = orthogonal_dimensions(dims)
    project_w_c = new_semantic(orthogonal_dims)
    
    print("Finish")
    
    
    
    
    