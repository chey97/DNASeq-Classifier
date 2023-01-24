import numpy as np #linear algebra
import pandas as pd #data processing, CSV I/O
import os
import matplotlib.pyplot as plt
#%matplotlib inline
for dirname, _,filenames in os.walk('../DNASeq Classifier/dna-sequence-dataset'): #give the specific path to the dstaset
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
#load human DNA data
human_dna = pd.read_table('/Users/chey/DNASeq Classifier/dna-sequence-dataset/human.txt')
human_dna.head()
