import numpy as np #linear algebra
import pandas as pd #data processing, CSV I/O
import os
import matplotlib.pyplot as plt
#%matplotlib inline
# for dirname, _,filenames in os.walk('../DNASeq Classifier/dna-sequence-dataset'): #specific path to the dstaset
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#---loading data----

#load human DNA data
human_dna = pd.read_table('../DNASeq Classifier/dna-sequence-dataset/human.txt')
print(human_dna.head())

#load chimpanzee DNA data
chimp_dna = pd.read_table('../DNASeq Classifier/dna-sequence-dataset/chimpanzee.txt')
chimp_dna.head()

#load dog DNA data
dog_dna = pd.read_table('../DNASeq Classifier/dna-sequence-dataset/dog.txt')
dog_dna.head()

#---plotting----

# Create a new subdirectory called "plots" if it does not exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Plot the class distribution of human DNA and save the plot
human_dna['class'].value_counts().sort_index().plot.bar(color='red')
plt.title("Class distribution of Human DNA")
plt.savefig("plots/Class_distribution_of_Human_DNA.png")
plt.show()

# Plot the class distribution of chimpanzee DNA and save the plot
chimp_dna['class'].value_counts().sort_index().plot.bar(color='blue')
plt.title("Class distribution of Chimpanzee DNA")
plt.savefig("plots/Class_distribution_of_Chimpanzee_DNA.png")
plt.show()

# Plot the class distribution of dog DNA and save the plot
dog_dna['class'].value_counts().sort_index().plot.bar(color='green')
plt.title("Class distribution of Dog DNA")
plt.savefig("plots/Class_distribution_of_Dog_DNA.png")
plt.show()

# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(10,5))

# Plot the class distribution of human DNA in the first subplot
human_dna['class'].value_counts().sort_index().plot.bar(ax=axs[0], color='red')
axs[0].set_title("Class distribution of Human DNA")

# Plot the class distribution of chimpanzee DNA in the second subplot
chimp_dna['class'].value_counts().sort_index().plot.bar(ax=axs[1], color='blue')
axs[1].set_title("Class distribution of Chimpanzee DNA")

# Plot the class distribution of dog DNA in the third subplot
dog_dna['class'].value_counts().sort_index().plot.bar(ax=axs[2], color='green')
axs[2].set_title("Class distribution of Dog DNA")

# Show the plots
plt.show()