# SCM
SCM_HW_HC = ['reliable','reserved','artistic', 'meditative','practical', 'important','industrious',  'cautious', 'serious','discriminating','intelligent', 'skillful', 'imaginative','scientific', 'determined'  ]
SCM_HW_LC = ['shrewd','honest','modest','tolerant','helpful','sincere','sentimental','humorous','good natured','happy','popular','sociable','warm','naive','submissive']
SCM_LW_HC = ['stern','critical','dominating','cold','unsociable','humorless','unpopular','pessimistic','irritable','moody','daring','persistent','unhappy','scientific','determined']                        
SCM_LW_LC = ['unhappy','vain','finicky', 'boring','unimaginative', 'dishonest', 'insignificant','superficial','squeamish','unintelligent', 'clumsy', 'impulsive','unreliable', 'foolish','frivolous', 'wasteful','wavering', 'irresponsible', 'submissive','naive']

# SD  # iongore it
SD_HW_HC = ['daring','reserved','discriminating','cautious','meditative','artistic','practical','serious','important','imaginative','persistent','scientific','determined','skillful','industrious','intelligent']
SD_HW_LC = ['shrewd','honest','modest','tolerant','helpful','sincere','sentimental','humorous','good natured','happy','popular','sociable','warm']
SD_LW_HC = ['stern','critical','dominating','cold','unsociable','humorless','unpopular','pessimistic','irritable','moody','unhappy','vain','finicky']                        
SD_LW_LC = ['unintelligent', 'clumsy', 'impulsive', 'unimaginative', 'unreliable', 'dishonest', 'insignificant', 'wavering', 'foolish', 'frivolous', 'submissive', 'irresponsible', 'naive', 'squeamish', 'superficial', 'wasteful', 'boring']

# SCM groups
# SCM_MAP = {'HW-HC': ['determined', 'intelligent', 'skillful', 'popular', 'imaginative', 'reliable', 'important', 'shrewd'], 'HW-LC': ['practical', 'industrious', 'warm', 'humorous', 'sociable', 'happy', 'honest', 'tolerant', 'modest', 'sincere', 'helpful', 'sentimental', 'scientific', 'artistic', 'meditative', 'reserved'], 'LW-LC': ['unintelligent', 'clumsy', 'cautious', 'impulsive', 'cold', 'irritable', 'humorless', 'unsociable', 'unpopular', 'unhappy', 'unimaginative', 'unreliable', 'dishonest', 'insignificant', 'foolish', 'frivolous', 'vain', 'submissive', 'irresponsible', 'naive', 'discriminating', 'squeamish', 'superficial', 'moody', 'pessimistic', 'wasteful', 'stern', 'finicky', 'boring'], 'LW-HC': ['persistent', 'wavering', 'critical', 'serious', 'daring', 'dominating']}

# SCM groups excluding ambiguous stereotype
# SCM_MAP = {'HW-LC': ['practical', 'industrious', 'warm', 'humorous', 'sociable', 'happy', 'tolerant', 'modest', 'sincere', 'helpful', 'sentimental', 'artistic', 'meditative'], 'HW-HC': ['intelligent', 'skillful', 'popular', 'imaginative', 'reliable', 'important'], 'LW-LC': ['unintelligent', 'clumsy', 'cautious', 'impulsive', 'cold', 'humorless', 'unsociable', 'unimaginative', 'unreliable', 'dishonest', 'insignificant', 'irresponsible', 'squeamish', 'superficial', 'wasteful', 'boring', 'unpopular'], 'LW-HC': ['wavering', 'serious', 'dominating']}

# POLAR groups
# SCM_MAP = {'HW-LC': ['determined', 'skillful', 'imaginative', 'persistent', 'shrewd', 'critical', 'discriminating', 'daring', 'stern', 'dominating'], 'HW-HC': ['practical', 'industrious', 'intelligent', 'cautious', 'warm', 'humorous', 'sociable', 'popular', 'happy', 'reliable', 'honest', 'important', 'wavering', 'tolerant', 'serious', 'modest', 'sincere', 'helpful', 'scientific', 'artistic', 'meditative'], 'LW-LC': ['unintelligent', 'clumsy', 'impulsive', 'cold', 'irritable', 'humorless', 'unsociable', 'unpopular', 'unhappy', 'unimaginative', 'unreliable', 'dishonest', 'foolish', 'frivolous', 'irresponsible', 'moody', 'wasteful', 'boring'], 'LW-HC': ['insignificant', 'vain', 'submissive', 'sentimental', 'naive', 'squeamish', 'superficial', 'pessimistic', 'finicky', 'reserved']}

# POLAR groups excluding ambiguous stereotype
SCM_MAP = {'HW-HC': ['practical', 'industrious', 'intelligent', 'cautious', 'warm', 'humorous', 'sociable', 'popular', 'happy', 'reliable', 'important', 'wavering', 'tolerant', 'serious', 'modest', 'sincere', 'helpful', 'artistic', 'meditative'], 'LW-LC': ['unintelligent', 'clumsy', 'impulsive', 'cold', 'humorless', 'unsociable', 'unimaginative', 'unreliable', 'dishonest', 'irresponsible', 'wasteful', 'boring', 'unpopular'], 'HW-LC': ['skillful', 'imaginative', 'dominating'], 'LW-HC': ['insignificant', 'sentimental', 'squeamish', 'superficial']}


def test_scm_robustness(SCM_MAP):
    for item in SCM_MAP.keys():
        # print(item)
        if item == 'LW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_LW_LC:
                    T += 1
                else:
                    # print('lw-lc:',val)
                    continue
            print("LW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'LW-HC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_LW_HC:
                    T += 1
            print("LW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        elif item == 'HW-LC':
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_HW_LC:
                    T += 1
            print("HW-LC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))
        else:
            item == 'HW-HC'
            T = 0
            for val in SCM_MAP[item]:
                if val in SCM_HW_HC:
                    T += 1
                else:
                    continue
                    #print("hw-hc:",val)
            print("HW-HC correct rate is {}".format(T/len(SCM_MAP[item])))
            print(T,len(SCM_MAP[item]))

test_scm_robustness(SCM_MAP)

