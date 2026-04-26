## 📌 Overview

This project is the official implementation of:

> **Stereotype Content Dictionary: A semantic space of 3 million words and phrases using Google News word2vec embeddings**  
> Xuanlong QIN & Tony Tam  
> SBP-BRiMS, 2023

Paper link: [Conference Proceeding](https://link.springer.com/chapter/10.1007/978-3-031-43129-6_2)

**Primary Maintainer:** Xuanlong QIN

This repository contains the code, experiments, and instructions to reproduce the results presented in the paper.

🌟 **I would also recommend you to read the relevant papers on this project.**

> **Embedding Social Perception Dimensions in a Semantic Space: Toward a Quantitative Synthesis**  
> Xuanlong QIN, Tony TAM 
> Journal of Social Computing, 2025

Paper link: [link](https://www.sciopen.com/article/10.23919/JSC.2025.0010)

and paper

> **Computational Evidence for the Two-Dimensional Structure of Social Evaluation: Pandemic-Era Insights From Americans’ Perceptions of Chinese and Japanese on Twitter**  
> Xuanlong QIN, Tony TAM 
> Social Science Computer Review, 2025

Paper link: [link](https://journals.sagepub.com/doi/10.1177/08944393261437640)

---


## Replication 
Before you start the project,there are some concepts need to be clarified. 

### 1. Preparation

1.1 Download Google news embedding, you could [click here](https://drive.google.com/file/d/1g3aw8PhEqsUhd3fo-qjolW_Y8xtn-qeL/view?usp=share_link) or find other public resources.

1.2 Set you coding environment
```
pip install -r requirements.txt
```

### 2. Introduction of the structure of this project
#### 2.1 Folder
bin : constructing Stereotype Content Dictionary by semantic differences
- SCM and POLAR is seperated.
- measure_stereotype: test Stereotype Content Dictionary
- measure_stereotype_POLAR: test POLAR framework


#### 2.2 Data

Antonmy: opposite pairs of POLAR and SCM model
- POLAR has 4 files
- SCM has 2 files(pair opposite dimensions)

Dictionaries: Fiske's Stereotype Content Dictionary
- It has 2 files, one for full dicionaries(14,000 words),amd another for seed dicionaries.

Verification 
- 64 commonly used personality traits (Rosenberg et al.,1968)

Experiment data
- Seed words from Fiske's dictionaries for building pairs


### 3. Code part
#### 1. Build Stereotype Content Dictionary
SCM's main code is `main_stereo.py` file; When you run this file you could get a semantic space of stereotype content with two dimensions.

POLAR's main code is `main_stereo_POLAR.py` file, run this file you could get a semantic space of stereotype content with two dimensions.

Note:
- `utils_stero.py` and `utils_stero_POLAR.py` both have `get_seed_words()` and `get_words()`, these two functions are independent functions, you can see there is no input.
- These two functions are basically used to filter word from Fiske's dictionaries for building pairs.

#### 2. Model validation
SCM_graph.py: find the categories of different words(SCM_MAP).
- you need to replace paths with different word embeddings

NOTE:
- groups: all 64 personality traits(actual 59).
- groups_boarder: all 64 personality traits excluding ambiguous stereotype(actual 39).

test_roubustness.py:
- test the accuracy, replace SCM_MAP

### 4. Result
For other research replicate this word more easily, We have uploaded Stereotype Content Dictionary to Harvard dataverse.

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




