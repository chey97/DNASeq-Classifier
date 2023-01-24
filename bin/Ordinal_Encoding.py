# In this approach, we need to encode each nitrogen bases as an ordinal value. 
# For example “ATGC” becomes [0.25, 0.5, 0.75, 1.0]. 
# Any other base such as “N” can be a 0.
# So let us create functions such as for creating a NumPy array object from a sequence string, and a label encoder with the DNA sequence alphabet “a”, “c”, “g” and “t”, but also a character for anything else, “n”.

import numpy as np
import re # Python "re" module provides regular expression support.

def string_to_array(seq_string):
    seq_string = seq_string.lower()
    seq_string = re.sub('[^acgt]','n', seq_string)
    seq_string = np.array(list(seq_string))
    return seq_string

#Create a label encoder with 'acgtn' alphabet
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
label_encoder.fit(np.array['a','c','g','t','z'])

#function to encode a DNA sequence string as an ordinal vector. 
# It returns a NumPy array with A=0.25, C=0.50, G=0.75, T=1.00, n=0.00.




