from scm_model import scm_semantic
import matplotlib.pyplot as plt


def find_groups():
    filePath = 'css_word_embedding/stereotype/data/verification/personality_traits.txt'
    groups = []
    with open(filePath,'r',encoding='utf-8') as fr:
        for line in fr:
            newline = line.rstrip().split(".")
            groups.append(newline[-1])
    return groups

def get_dimensions(groups):
    SCM_MAP = dict()
    for group in groups:
        val = scm_semantic(group)
        if val is None:
            print(group)
        else:
            try:
                if val[1][0] > 0 and val[1][1]> 0 :
                    if 'HW-HC' in SCM_MAP.keys():
                        SCM_MAP['HW-HC'].append(group)
                    else:
                        SCM_MAP['HW-HC'] = [group]
                        
                elif val[1][0] > 0 and val[1][1] < 0:
                    if 'HW-LC' in SCM_MAP.keys():
                        SCM_MAP['HW-LC'].append(group)
                    else:
                        SCM_MAP['HW-LC'] = [group]
                        
                elif val[1][0] < 0 and val[1][1] < 0:
                    if 'LW-LC' in SCM_MAP.keys():
                        SCM_MAP['LW-LC'].append(group)
                    else:
                        SCM_MAP['LW-LC'] = [group]
                        
                else:
                    if 'LW-HC' in SCM_MAP.keys():
                        SCM_MAP['LW-HC'].append(group)
                    else:
                        SCM_MAP['LW-HC'] = [group]
            except Exception as e:
                print(e)
        #print(SCM_MAP)
    return SCM_MAP
            
            
    
            
def draw_pic(groups):
    warmth = []
    competent = []
    text =[]

    for g in groups:
        val = scm_semantic(g)
        print(val)
        if val == None:
            continue
        else:
            text.append(val[0])
            warmth.append(val[1][0])
            competent.append(val[1][1])


    plt.xlim((-1, 1))
    plt.ylim((-1, 1))
    plt.scatter(warmth, competent)
    for i in range(len(text)):
        plt.annotate(text[i], xy = (warmth[i], competent[i]), xytext = (warmth[i]-0.1, competent[i]+0.2))
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # groups = find_groups()   
    # 'high-strung','good natured' had lost 
    # all 64 personality traits.(actual 59)
    groups = ['determined', 'practical', 'industrious', 'intelligent', 'unintelligent', 'skillful', 'clumsy', 'cautious', 
              'impulsive', 'warm', 'cold', 'irritable',  'humorous', 'humorless', 'sociable', 'unsociable',
              'popular', 'unpopular', 'happy', 'unhappy', 'imaginative', 'unimaginative', 'reliable', 'unreliable', 'honest',
              'dishonest', 'important', 'insignificant', 'persistent', 'wavering', 'foolish', 'shrewd', 'critical', 'tolerant', 
              'serious', 'frivolous', 'vain', 'modest', 'submissive', 'irresponsible', 'sincere', 'helpful', 'sentimental',
              'naive', 'scientific', 'discriminating', 'squeamish', 'daring', 'superficial', 'moody', 'pessimistic', 'wasteful', 
              'stern', 'finicky', 'artistic', 'meditative', 'dominating', 'boring', 'reserved']
    
    #'inventive','liar','egotistical'
    # all 64 personality traits excluding ambiguous stereotype.(actual 39)
    groups_boarder = ['practical', 'industrious', 'intelligent', 'unintelligent', 'skillful', 'clumsy', 'cautious', 
              'impulsive', 'warm', 'cold',  'humorous', 'humorless', 'sociable', 'unsociable',
              'popular', 'happy',  'imaginative', 'unimaginative', 'reliable', 'unreliable', 
              'dishonest', 'important', 'insignificant',  'wavering',  'tolerant', 
              'serious',  'modest', 'irresponsible', 'sincere', 'helpful', 'sentimental',
              'squeamish',  'superficial',  'wasteful', 
               'artistic', 'meditative', 'dominating', 'boring', 'unpopular']
    # draw_pic(groups)
    print(len(groups),len(groups_boarder))
    scm_map = get_dimensions(groups_boarder)
    print(scm_map)

            

    


    




