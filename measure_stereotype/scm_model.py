import numpy as np
import re
def scm_semantic(search_val):
    """search word and return its vector

    Args:
        search_val (str): the word you want to search

    Returns:
        array: np.array
    """
    
    # SCM_model = 'css_word_embedding/stereotype/data/semantic_stereotype/POLAR_embedding_final.bin'
    # SCM_model = 'css_word_embedding/stereotype/data/semantic_stereotype/SD_embedding_final.bin'
    SCM_model = 'css_word_embedding/stereotype/data/semantic_stereotype/SCM_embedding_final.bin'
    with open(SCM_model,'r') as f:
        # next(f)
        try:
            for line in f:
                # print(line)
                key = line.replace('"','').split(',')[0]
                if key == search_val:
                    dimension = np.array(re.findall(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?",line)).astype('float64')
                    return (key,dimension)
                else:
                    continue
        except IOError:
            print("Input errot check the line {}".format(line))
        
        except Exception as e:
            print('err is :',e )
            print(line + "can not found")
            
