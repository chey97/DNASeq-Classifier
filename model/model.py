'''
DNASeq - DNA Sequence Classifier Copyright (C) 2023  Chethiya Galkaduwa
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See theGNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
- This program was build for academic purpose -
'''

import numpy as np #linear algebra
import pandas as pd #data processing, CSV I/O
import os
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer 

#%matplotlib inline
# for dirname, _,filenames in os.walk('../DNASeq Classifier/dna-sequence-dataset'): #specific path to the dstaset
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

#------loading data-------

#load human DNA data
human_dna = pd.read_table('../DNASeq-Classifier/dna-sequence-dataset/human.txt')
(human_dna.head())
#print((human_dna.head()))

#load chimpanzee DNA data
chimp_dna = pd.read_table('../DNASeq-Classifier/dna-sequence-dataset/chimpanzee.txt')
chimp_dna.head()

#load dog DNA data
dog_dna = pd.read_table('../DNASeq-Classifier/dna-sequence-dataset/dog.txt')
dog_dna.head()

#------plotting-------

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
if not os.path.exists("plots"):
    os.makedirs("plots")

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

# Save the figure
fig.savefig("plots/Class_distribution_of_DNA.png")
# Show the plots
#plt.show()

#k-mers function
def Kmers_funct(seq, size=6):
    return [seq[x:x+size].lower() for x in range(len(seq) - size + 1)]

#------conversion------

#convert our training data sequences into short overlapping k-mers of length 6 for each species of data.

human_dna['words'] = human_dna.apply(lambda x: Kmers_funct(x['sequence']), axis=1)
human_dna = human_dna.drop('sequence', axis=1)

'''---
1. human_dna['words'] =: This creates a new column in the human_dna dataframe called words.
2. human_dna.apply(lambda x:: This uses the apply() function to apply a user-defined function to each row of the human_dna dataframe. The lambda x: is an anonymous function that is passed to the apply() function and takes the value of the current row as the input argument.
3. Kmers_funct(x['sequence']),: This is the user-defined function Kmers_funct() that takes the sequence column of the current row as the input argument. It is applied to each row of the dataframe, and the output of the function is stored in the new words column.
4. axis=1): This specifies that the function Kmers_funct() is applied along the rows (axis=1) of the dataframe.
5. human_dna = human_dna.drop('sequence', axis=1): This line drops the 'sequence' column from the dataframe using the drop() function, with axis=1 indicating that the column is dropped from the dataframe along the columns axis.
----'''

chimp_dna['words'] = chimp_dna.apply(lambda x: Kmers_funct(x['sequence']), axis=1)
chimp_dna = chimp_dna.drop('sequence', axis=1)

dog_dna['words'] = dog_dna.apply(lambda x: Kmers_funct(x['sequence']), axis=1)
dog_dna = dog_dna.drop('sequence', axis=1)

#print(human_dna.head())

#convert the lists of k-mers for each gene into string sentences of words that can be used to create the Bag of Words model

human_texts = list(human_dna['words'])
for item in range(len(human_texts)):
    human_texts[item] = ' '.join(human_texts[item])
#separate labels
y_human = human_dna.iloc[:, 0].values # y_human for human_dna

#print(human_texts)
#print(y_human)

chimp_texts = list(chimp_dna['words'])
for item in range(len(chimp_texts)):
    chimp_texts[item] = ' '.join(chimp_texts[item])
#separate labels
y_chim = chimp_dna.iloc[:, 0].values # y_chim for chimp_dna

dog_texts = list(dog_dna['words'])
for item in range(len(dog_texts)):
    dog_texts[item] = ' '.join(dog_texts[item])
#separate labels
y_dog = dog_dna.iloc[:, 0].values  # y_dog for dog_dna

#------Creating the Bag of Words model using CountVectorizer()------

cv = CountVectorizer(ngram_range=(4,4)) #the n-gram size of 4 is previously detemined by testing.
X = cv.fit_transform(human_texts) #use fit_transform() on training data but transform() on the test data
X_chimp = cv.transform(chimp_texts)
X_dog = cv.transform(dog_texts)
#F = cv.get_feature_names_out()
    

#print(cv.get_feature_names_out())

print("Number of human genes converted into uniform length feauture vectors of k-mer counts  :",X.shape)
print("Number of chimpanzee genes converted into uniform length feauture vectors of k-mer counts  :",X_chimp.shape)
print("Number of dog genes converted into uniform length feauture vectors of k-mer counts  :",X_dog.shape)
    

'''
Should output these : So, for humans 4380 genes converted into uniform length feature vectors of 4-gram k-mer (length 6) counts. 
For chimp and dog, the same number of features with 1682 and 820 genes respectively.
X       - (4380, 232414)
X_chimp - (1682, 232414)
X_dog   - (820, 232414)
'''

# df = pd.DataFrame(F)
# print(df)
# df.to_csv('human_feautures.csv')
