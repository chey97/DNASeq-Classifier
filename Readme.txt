DNA data handling using Biopython

In the model.py there is a  brief example of how to work with a DNA sequence in fasta format using Biopython. 
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

The purdpose of this model is to classify gene families based on the DNA sequence of the coding sequence. 
This can be useful in understanding genetic variation and evolution across different species, as well as in identifying specific genes and genetic markers for medical and biological research.
By trainning the model of human DNA sequences and testing it on the DNA sequences of other species, like chimpanzees and dogs, can determine the models ability to accurartely classify gene families across different species and evaluate its potential applicability to other organisms.

_______________________

Definitions for each of the 7 classes in the human training data:
![Alt text](/DNASeq Classifier/images/7 classes in the human trainning data.png)


To learn about CountVectorizer : https://pianalytix.com/countvectorizer-in-nlp/
                               : https://docs.google.com/document/d/1Tez9aljU6ccZVG0cDI_0I4UeI9hjuQ0uc7WQKnwJqgY/edit#heading=h.mnzfhaloi4d6

CountVectorizer and Ngram tutorial : https://www.kaggle.com/code/shaukathussain/countvectorizer-and-ngram-tutorial-for-beginners/notebook

Why we use fit_transform() on training data but transform() on the test data?
https://towardsdatascience.com/what-and-why-behind-fit-transform-vs-transform-in-scikit-learn-78f915cf96fe
We call fit_transform() method on our training data and transform() method on our test data.

fit_transform() -   The fit method is calculating the mean and variance of each of the features present in our data. 
                    The transform method is transforming all the features using the respective mean and variance.

transform()     -   Using the transform method we can use the same mean and variance as it is calculated from our training data to transform our test data. 
                    Thus, the parameters learned by our model using the training data will help us to transform our test data.


Here I have used the human data to train the model, holding out 20% of the human data to test the model. 
Then I can challenge the model’s generalizability by trying to predict sequence function in other species (the chimpanzee and dog).

Multinomial Naїve Bayes’ For Documents Classification and Natural Language Processing (NLP) : https://towardsdatascience.com/multinomial-naïve-bayes-for-documents-classification-and-natural-language-processing-nlp-e08cc848ce6



This program was build for academic purpose - DNASeq - DNA Sequence Classifier Copyright (C) 2023  Chethiya Galkaduwa
