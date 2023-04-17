import numpy as np
from scm_model import scm_semantic
import matplotlib.pyplot as plt

with open('css_word_embedding/stereotype/antonmy/POLAR_competent_high.csv','r') as infile:
    competent_high = infile.readlines()

with open('css_word_embedding/stereotype/antonmy/POLAR_competent_low.csv','r') as infile:
    competent_low = infile.readlines()

with open('css_word_embedding/stereotype/antonmy/POLAR_warmth_high.csv','r') as infile:
    warmth_high = infile.readlines()

with open('css_word_embedding/stereotype/antonmy/POLAR_warmth_low.csv','r') as infile:
    warmth_low = infile.readlines()

def getwordVec(words):
    vecs = []
    for word in words:
        word = word.replace('\n', '')
    
        try:
            val = scm_semantic(word)
            # print(val[1])
            vecs.append(list(val[1]))
        except Exception as e:
            print(e)
    return vecs

competent_high_vecs = getwordVec(competent_high)
competent_low_vecs = getwordVec(competent_low)
warmth_high_vecs = getwordVec(warmth_high)
warmth_low_vecs = getwordVec(warmth_low)

competent_high_x =[]
competent_high_y =[]
competent_low_x = []
competent_low_y = []


warmth_high_x = []
warmth_high_y = []
warmth_low_x = []
warmth_low_y = []

for i in range(len(competent_high_vecs)):
    competent_high_x.append(competent_high_vecs[i][0])
    competent_high_y.append(competent_high_vecs[i][1])

for i in range(len(competent_low_vecs)):
    competent_low_x.append(competent_low_vecs[i][0])
    competent_low_y.append(competent_low_vecs[i][1])

for i in range(len(warmth_high_vecs)):
    warmth_high_x.append(warmth_high_vecs[i][0])
    warmth_high_y.append(warmth_high_vecs[i][1])
    
for i in range(len(warmth_low_vecs)):
    warmth_low_x.append(warmth_low_vecs[i][0])
    warmth_low_y.append(warmth_low_vecs[i][1])
    



# fig = plt.figure()
ax = plt.subplot(1,2,1)
ax.scatter(competent_high_x, competent_high_y,color='red',alpha = 0.2)
ax.scatter(competent_low_x,competent_low_y,color='green' ,alpha = 0.2)
ax.set_title("competent")
ax.set_xlabel("competent")

ax2 = plt.subplot(1,2,2)
ax2.scatter(warmth_high_x, warmth_high_y,color='yellow',marker = 'v',alpha = 1)
ax2.scatter(warmth_low_x,warmth_low_y,color='purple' ,marker = 'v',alpha = 1)
ax2.set_title("warmrth")
ax2.set_xlabel("warmrth")

plt.suptitle("Segregation of Stereotypes")
plt.savefig('figure2.jpg')
plt.show()