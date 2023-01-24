DNA data handling using Biopython

In the main.py there is a  brief example of how to work with a DNA sequence in fasta format using Biopython. 
The sequence object will contain attributes such as id and sequence and the length of the sequence that you can work with directly.

We will use Bio.SeqIO from Biopython for parsing DNA sequence data(fasta). 
It provides a simple uniform interface to input and output assorted sequence file formats.

-----------------------

We can load and manipulate biological sequence data easily, how can we use it for machine learning or deep learning?

Now since machine learning or deep learning models require input to be feature matrices or numerical values and currently we still have our data in character or string format. 
So the next step is to encode these characters into matrices.

There are 3 general approaches to encode sequence data:

1. Ordinal encoding DNA Sequence

2. One-hot encoding DNA Sequence

3. DNA sequence as a “language”, known as k-mer counting

-----------------------

Objective: Build a classification model that is trained on the human DNA sequence and can predict a gene family based on the DNA sequence of the coding sequence. 

To test the model, we will use the DNA sequence of humans, dogs, and chimpanzees and compare the accuracies.

The dataset contains human DNA sequence, Dog DNA sequence, and Chimpanzee DNA sequence.
_______________________

Definitions for each of the 7 classes in the human training data:
![Alt text](/DNASeq Classifier/images/7 classes in the human trainning data.png)


To learn about CountVectorizer : https://pianalytix.com/countvectorizer-in-nlp/
                               : https://docs.google.com/document/d/1Tez9aljU6ccZVG0cDI_0I4UeI9hjuQ0uc7WQKnwJqgY/edit#heading=h.mnzfhaloi4d6

CountVectorizer and Ngram tutorial : https://www.kaggle.com/code/shaukathussain/countvectorizer-and-ngram-tutorial-for-beginners/notebook