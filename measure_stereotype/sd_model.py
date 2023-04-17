import pandas as pd
import numpy as np 
import gensim 

embedding_path = 'css_word_embedding/stereotype/GoogleNews-vectors-negative300.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(embedding_path,binary=True)


def get_word():
    osgood_path = 'css_word_embedding/stereotype/data/verification/Jenkins_1958_data.csv'
    df = pd.read_csv(osgood_path,delimiter=',')
    print(df.shape,df.index)
    print(df.head())
    df['Word'] = df['Word'].str.lower()
    df_new = df[['Word','S8','S11']]
    print(df_new.describe())
    df_new.to_csv('css_word_embedding/stereotype/data/verification/Jenkins_1958_potency_evaluation.csv')
    # df_new_filter_s8 = df_new[df_new['S8'] > 483]
    # df_new_filter_s11 = df_new[df_new['S11'] > 458.5]
    # print(df_new_filter_s8,df_new_filter_s11)

def get_antonym(word_list):


    for i in range(len(word_list)):
        positive=['good']
        negative = ['bad']
        positive.append(word_list[i])
        print(positive)
        val = model.most_similar(positive, negative)
        print(val,val[0][0])

def get_positive_word():
    wordlist = []
    path = 'css_word_embedding/stereotype/antonmy/SD_potency_pairs.csv'
    with open(path,'r',encoding='utf-8') as f:
        for i in f:
            newline = i.strip().split(',')[0]
            wordlist.append(newline)
            #print(newline)
    print(wordlist)
    return wordlist

if __name__ == '__main__':
    # get_word()
    
    word_list = get_positive_word()
    get_antonym(word_list)