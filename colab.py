# -*- coding: utf-8 -*-
"""Copy of Iris_Scikit_Learn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VZkmtpC0sPeCvnwHm0VYntxXEKg_4Nhl

##Disclaimer
This code is taken from this [notebook](https://colab.research.google.com/drive/1XSnIhSIsw3LMc6mkXlw66sMc7ZwFAJKT?usp=sharing). I only take the important part of Decision Tree Learning and adding the code to save the models.

---

##Continue the Learning!

Now that you have one classification technique down, let's try another, **Decision Trees**. We will also be discuss a way to analyze accuracy called a **Confusion Matrix**.


##Decision Trees: Importing and Cleaning up the Data
We already loaded the data in the beginning. Let's load it again, just in case you are starting to run the code from here.
"""

#Import required libraries
import pandas as pd #loading data in table form
import numpy as np # linear algebra
from sklearn.tree import DecisionTreeClassifier #Creating the Decision Tree
from sklearn import tree#Visualizing the Decision Tree
# import graphviz #Visualizing the Decision Tree
from sklearn.metrics import confusion_matrix #Confusion Matrix
# import matplotlib.pyplot as plt #visualization
from sklearn.datasets import load_iris

# Load the dataset, which contains the examples and their labels
iris_dataset = load_iris()

"""## Decision Tree: Splitting up the training and test sets

Remember that in classification, which is a type of supervised machine learning, we must use a training set to teach our model how to correctly classify future examples. We also use a test set to test how good our model is.

The first step that we'll do is break up the Iris dataset into training set and test set:
"""

from sklearn.model_selection import train_test_split

# Break the dataset up into the examples (X) and their labels (y)
X, y = iris_dataset.data, iris_dataset.target

# Split up the X and y datasets into train and test sets
# 25% of the dataset will be used for the test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=31)

"""Our training set contains all of the correct targets (classes) for our flower examples, along with the four features of each flower. We'll need all of this information to teach our classifier how to predict a class given a new set of four features.

**Note: Because the data points are split randomly into train and test, each run might not be the same**

## Decision Tree: Training our Classifier

As Decision Trees are a well-known classifier. There is already a library with a function to make one. You can always create it from scratch, but sometimes using the library function is less tedius. When you need to customize more advanced aspects of the classifier, it makes sense to start from scratch, unlike here.
"""

# sklearn classifiers built in
# We're going to import the decision tree classifier
from sklearn.tree import DecisionTreeClassifier

# Initialize the classifier with a max_depth of 5
classifier = DecisionTreeClassifier(max_depth=5)

# Fit the classifier to the training set
classifier = classifier.fit(X_train, y_train)

"""##Decision Tree: Testing
We've trained our decision tree and visualized it, but we have not yet tested it to see how well it does. This is where the test set comes in -- the test set is a set of correctly labelled examples that we have withheld from the decision tree, so we can test to see if the predictions made by the decision tree match the correct labels.

With `sklearn`, it's really easy to generate our predicted labels for the test set:

"""

# Create a list of predicted classes for each of the examples in the test set
y_predict = classifier.predict(X_test)

"""In order to find the accuracy of our classifier on the test set, we use the function `score()`, which takes two parameters: (1) the data of the test set, and (2) the correct labels of the test set.

It will automatically compare our predicted label with the correct label to compute the accuracy.
"""

accuracy = classifier.score(X_test, y_test)
print(accuracy)

"""##Save Model
Save model using joblib
"""

import joblib

filename = 'model.sav'
joblib.dump(classifier, filename)

"""## Load Model
To make sure that the saved models are work as expected
"""

# load the model from disk
loaded_model = joblib.load(filename)

result = loaded_model.score(X_test, y_test)
print(result)