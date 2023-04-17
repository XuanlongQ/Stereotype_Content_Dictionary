import numpy as np
from embedding_common import word2vec_fun
def normalize_vector(x):
    """Normalize vector

    Args:
        x (array): _description_

    Returns:
        array: _description_
    """
    return x/np.linalg.norm(x) 

def get_culture_dimension(x,y):
    """get dimensions of culture

    Args:
        x (str): first word of anti pair
        y (str): second word of anti pair

    Returns:
        array: normalized vectors of cultual dimension
    """
    nrm_x = normalize_vector(x)
    nrm_y = normalize_vector(y)
    dimension = normalize_vector(nrm_x - nrm_y)
    # print(dimension)
    return dimension
    
def build_dimensions(anti_pairs):
    """create characteristic dimension

    Args:
        anti_pairs (array): anti pairs

    Returns:
        array: normalized mean value of vector
    """
    # da = dict()
    word_dims = np.full((anti_pairs.shape[0], 300), np.nan) # create matrix
    for _ in range(anti_pairs.shape[0]):
        print(_)
        rp_word_0 = anti_pairs[_,0]
        rp_word_1 = anti_pairs[_,1]
        try:
            rp_word_vec_0, rp_word_vec_1 = word2vec_fun(str(rp_word_0),str(rp_word_1))
            # word_dims[_,] = get_culture_dimension(rp_word_vec_0, rp_word_vec_1)
            word_dims[_,] = rp_word_vec_0 - rp_word_vec_1
            # da[rp_word_0] = rp_word_vec_0 - rp_word_vec_1
        except Exception as err:
            print("something wrong, the err is{}".format(err))
    
    # import pandas as pd        
    # df = pd.DataFrame(da)
    # d = df.T
    # d.to_csv('sample_competent.csv')
    
    dim_ave = np.nanmean(word_dims,axis=0)
    dim_ave_n = normalize_vector(dim_ave)
    return dim_ave_n

def get_antonym_pairs(ant_pairs_aff_path):
    """get antonym pairs from path

    Args:
        ant_pairs_aff_path (str): path of antonym pairs

    Returns:
        array: put antonym pairs in one array
    """
    import csv
    ant_pairs = []
    with open(ant_pairs_aff_path,'r') as f:
        reader = csv.reader(f)
        for line in reader:
            line = [x.lower() for x in line]
            # print(line,type(line))
            ant_pairs.append(np.array(line))
    ant_pairs_content = np.vstack(ant_pairs)
    return ant_pairs_content
    

def get_seed_words():
    import pandas as pd
    seedWords_path = 'css_word_embedding/stereotype/data/dictionary/osfstorage-archive/Dictionaries/Seed Dictionaries.csv'

    df = pd.read_csv(seedWords_path,delimiter=',')
    
    print(df.shape)
    # high-warmth
    df['Sociability_dict_hi'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Sociability' and x['Dir'] == 'high' else 0 ,axis = 1)
    df['Morality_dict_hi'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Morality' and x['Dir'] == 'high' else 0 ,axis = 1)
    # if one high then warmth is high
    df['Warmth_dict_hi'] = df.apply(lambda x: 0 if x['Sociability_dict_hi'] + x['Morality_dict_hi'] == 0 else 1,axis = 1)
    # print(df[df['Warmth_dict_hi']==1])
    
    # low-warmth
    df['Sociability_dict_lo'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Sociability' and x['Dir'] == 'low' else 0 ,axis = 1)
    df['Morality_dict_lo'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Morality' and x['Dir'] == 'low' else 0 ,axis = 1)
    # if one low then warmth is low
    df['Warmth_dict_lo'] = df.apply(lambda x: 0 if x['Sociability_dict_lo'] + x['Morality_dict_lo'] == 0 else 1,axis = 1)
    # print(df[df['Warmth_dict_hi']==0])
    
    # high-competence
    df['Ability_dict_hi'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Ability' and x['Dir'] == 'high' else 0 ,axis = 1)
    df['Agency_dict_hi'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Agency' and x['Dir'] == 'high' else 0 ,axis = 1)
    # if one high then competent is high
    df['Competence_dict_hi'] = df.apply(lambda x: 0 if x['Ability_dict_hi'] + x['Agency_dict_hi'] == 0 else 1,axis = 1)
    # print(df[df['Competence_dict_hi']==0])
    
    # low-competence
    df['Ability_dict_lo'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Ability' and x['Dir'] == 'low' else 0 ,axis = 1)
    df['Agency_dict_lo'] = df.apply(lambda x: 1 if x['Dictionary'] == 'Agency' and x['Dir'] == 'low' else 0 ,axis = 1)
    # if one low then competent is low
    df['Competence_dict_lo'] = df.apply(lambda x: 0 if x['Ability_dict_lo'] + x['Agency_dict_lo'] == 0 else 1,axis = 1)
    # print(df[df['Competence_dict_lo']==0])
    
    cols_warmth=['Dictionary','term','Dir','Warmth_dict_hi','Warmth_dict_lo']
    cols_competent = ['Dictionary','term','Dir','Competence_dict_hi','Competence_dict_lo']
    
    
    df.to_csv('test_warm.csv',columns = cols_warmth)
    df.to_csv('test_competent.csv',columns = cols_competent)
            
def get_words():
    path = 'test_competent.csv'
    import csv
    with open(path,'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line[3] == 'high':
                print(line)
                with open('css_word_embedding/stereotype/antonmy/POLAR_competent_high.csv','a+',encoding='utf-8') as fw:
                    fw.write(line[2] +'\n')
                    fw.close()
            
 
    