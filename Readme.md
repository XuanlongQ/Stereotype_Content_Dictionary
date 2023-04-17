## Stereotype Content Dictionary: A semantic space of 3 million words and phrases using Google News word2vec embeddings

*Note: This readme for how to constructing a Stereotype Content Dictionary based on word embeddings, more detail please refer to the paper.*

Before we start the project,there are some preparation and concepts need to clarify. please follow this guideline

### 1. Preparation

1.1 Download Google news embedding, you could [click here](https://drive.google.com/file/d/1g3aw8PhEqsUhd3fo-qjolW_Y8xtn-qeL/view?usp=share_link) or find other public resources.

1.2 Set you coding environment
```
pip install -r requirements.txt
```

### 2. Introduction of the structure of my project
#### 2.1 Folder
bin : constructing Stereotype Content Dictionary by semantic differences
- SCM and POLAR is seperated.
measure_stereotypr: test Stereotype Content Dictionary
- SCM and POLAR is seperated.

#### 2.2 Data

antonmy: opposite pairs of POLAR and SCM model
- POLAR has 4 files
- SCM has 2 files(pair opposite dimensions)

dictinoaries: Fiske's Stereotype Content Dictionary
- it has 2 files, one for Full dicionaries(14,000 words),another for seed dicionaries.

verification
- 64 commonly used personality traits

experiment data
- filter words from Fiske's dictionaries for build pairs


### Code part
#### 1. Build Stereotype Content Dictionary
*NOTE: Detail interpretation please check the code, this is a rough illustration *

SCM's main code is main_stereo.py, run this file you could get a semantic space of stereotype content with two dimensions.

POLAR's main code is main_stereo_POLAR.py, run this file you could get a semantic space of stereotype content with two dimensions.

Note:
- utils_stero.py and utils_stero_POLAR.py both have get_seed_words() and get_words(), these two functions are independent function, you could see there is no input.
- these two function is used to filter word from Fiske's dictionaries for building pairs.

#### 2. Model verifivation
SCM_graph.py: find the categories of different words(SCM_MAP).
- you need to replace different word embeddings

NOTE:
- groups: all 64 personality traits.(actual 59)
- groups_boarder: all 64 personality traits excluding ambiguous stereotype.(actual 39)

test_roubustness.py:
- test the accuracy, replace SCM_MAP

### Result
For other research replicate this word more easily, i have uploaded Stereotype Content Dictionary to Harvard dataverse.
Dataset will be publised after this paper has been accepted.

Citation format as follows:
```
@data{DVN/OUXIYW_2023,
author = {qin, xuanlong},
publisher = {Harvard Dataverse},
title = {{Replication Data for: Stereotype Content Dictionary: A semantic space of 3 million words and phrases using Google News word2vec embeddings}},
year = {2023},
version = {DRAFT VERSION},
doi = {10.7910/DVN/OUXIYW},
url = {https://doi.org/10.7910/DVN/OUXIYW}
}
```

**Please feel free to contact me**




