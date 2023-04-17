import time
import gensim
import numpy as np
from fun import cosine_similarity


model_path = 'css_word_embedding/stereotype/GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_path,binary=True)


def print_run_time(func):
    """
    decorate function for recording function running time
    """  
    def wrapper(*args, **kw):  
        local_time = time.time()  
        func(*args, **kw) 
        print ('current Function {} run time is {}'.format(func.__name__ ,time.time() - local_time)  )
    return wrapper 


def word2vec_fun(*args):
    """word pairs

    Returns:
        array: embedding vector
    """
    print(args[0],args[1])
    vec_0 = model[args[0]]
    vec_1 = model[args[1]]
    return vec_0,vec_1
               
def orthogonal_dimensions(dims):
    """orthogonalized dimensions

    Args:
        dims (array): dimensions of model

    Returns:
        array: orthogonalized dimensions
    """
    beta1 = dims[0]
    a2 = dims[1]
    beta2 = a2 - np.dot(a2,beta1) * beta1 / np.dot(beta1,beta1)
    
    newdims = np.vstack((beta1,beta2))
    return newdims

def new_semantic(dim):
    """dimensions of new semantic space

    Args:
        dim (array): the array of new dimensions of new semantic space
    """
    curr_antonmy_vector = np.linalg.pinv(np.transpose(dim))
    print(curr_antonmy_vector)   
    vocab_list = model.index_to_key

    for each_word in vocab_list:
        new_vector = np.matmul(curr_antonmy_vector,model[each_word])
        new_vector = new_vector/np.linalg.norm(new_vector)
        with open('css_word_embedding/stereotype/data/semantic_stereotype/SCM_embedding_final.bin','a+',encoding='utf-8') as f:
            f.write(each_word + ',' + str(new_vector[0]) + ',' + str(new_vector[1]) + '\n')
            f.close()
        
def filter_pairs(ant_pairs):
    """find suitable pairs
    
    Args:
        ant_pairs (array): anti pairs of warmth

    Returns:
        array: selected anti pairs,The filter parameter is 0.5 now 
    """
    pair_list = []
    for pair in ant_pairs:
        try:
            val = cosine_similarity(model[pair[0]],model[pair[1]])
            if val < 0.5:
                pair_list.append(pair)
                print(pair,val)
            else:
                continue   
        except Exception as e:
            print(e)
    # print(pair_list,len(pair_list))
    return np.array(pair_list)
    