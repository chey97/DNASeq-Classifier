'''
- This program was build for academic purpose - DNASeq - DNA Sequence Classifier Copyright (C) 2023  Chethiya Galkaduwa
'''

# Another approach is to use one-hot encoding to represent the DNA sequence. 
# This is widely used in deep learning methods and lends itself well to algorithms like convolutional neural networks. 
# This example, “ATGC” would become [0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]. And these one-hot encoded vectors can either be concatenated or turned into 2-dimensional arrays.



from sklearn.preprocessing import LabelEncoder
from Ordinal_Encoding import string_to_array
import numpy as np

# Create a label encoder with 'acgtn' alphabet
label_encoder = LabelEncoder()
label_encoder.fit(np.array(['a','c','g','t','z']))

from sklearn.preprocessing import OneHotEncoder

def one_hot_encoder(seq_string):
    int_encoded = label_encoder.transform(seq_string)
    onehot_encoder = OneHotEncoder(sparse=False, dtype=int)
    int_encoded = int_encoded.reshape(len(int_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(int_encoded)
    onehot_encoded = np.delete(onehot_encoded, -1, 1)
    return onehot_encoded


    
# try out with a simple short sequence:
seq_test = 'GAATTCTCGAA'
print(one_hot_encoder(string_to_array(seq_test)))