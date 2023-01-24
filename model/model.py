import numpy as np #linear algebra
import pandas as pd #data processing, CSV I/O
import os
import matplotlib.pyplot as plt
#%matplotlib inline
# for dirname, _,filenames in os.walk('../DNASeq Classifier/dna-sequence-dataset'): #specific path to the dstaset
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
        
#load human DNA data
human_dna = pd.read_table('../DNASeq Classifier/dna-sequence-dataset/human.txt')
print(human_dna.head())

#Plot the human DNA data, Subdir - plots
script_dir = os.path.dirname('DNASeq Classifier')
results_dir = os.path.join(script_dir, 'plots/')
sample_file_name = "Class_distribution_of_Human_DNA"

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)

human_dna['class'].value_counts().sort_index().plot.bar()
plt.title("Class distribution of Human DNA")
plt.savefig(results_dir + sample_file_name)

