'''
Here the human data is used to train the model, holding out 20% of the human data to test the model.
Then challenge the model's generalizability by trying to predict sequence function in other species (the chimpanzee and dog).
Next, train/test split human dataset and build simple multinomial naive Bayes classifier.
'''
import model
import numpy as np #linear algebra
import pandas as pd #data processing, CSV I/O
import os
import matplotlib.pyplot as plt

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

#------Splitting the human dataset into the training set and test set------
X = model.X
y_human = model.y_human
X_train, X_test, y_train, y_test = train_test_split(X,y_human,test_size = 0.20,random_state=42)

#------create a multinomial naive Bayes classifier------

classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#model performce metrics like the confusion matrix, accuracy, precision, recall and f1 score.

print("Confusion matrix for predictions on human test DNA sequence\n")
print(pd.crosstab(pd.Series(y_test, name='Actual'), pd.Series(y_pred, name='Predicted')))
def get_metrics(y_test, y_predicted):
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='weighted')
    recall = recall_score(y_test, y_predicted, average='weighted')
    f1 = f1_score(y_test, y_predicted, average='weighted')
    return accuracy, precision, recall, f1
accuracy, precision, recall, f1 = get_metrics(y_test, y_pred)
print("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f" % (accuracy, precision, recall, f1))




