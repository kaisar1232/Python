import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter

# Ignore FutureWarnings
simplefilter(action='ignore', category=FutureWarning)

# Print information about the project and dataset
print("--- Marvellous Infosystems by Piyush Khairnar -----")
print("---- Diabetes predictor using Logistic Regression -----")

# Load the diabetes dataset
diabetes = pd.read_csv('diabetes.csv')

# Print the columns of the dataset
print("Columns of Dataset:")
print(diabetes.columns)

# Print the first 5 records of the dataset
print("First 5 records of dataset:")
print(diabetes.head())

# Display the dimensions of the diabetes data
print("Dimension of diabetes data: {}".format(diabetes.shape))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

# Train a logistic regression model
logreg = LogisticRegression().fit(X_train, y_train)

# Print the training set accuracy
print("Training set accuracy: {:.3f}".format(logreg.score(X_train, y_train)))

# Print the test set accuracy
print("Test set accuracy: {:.3f}".format(logreg.score(X_test, y_test)))

# Train another logistic regression model with a different regularization parameter
logreg001 = LogisticRegression(C=0.01).fit(X_train, y_train)

# Print the training set accuracy for the new model
print("Training set accuracy: {:.3f}".format(logreg001.score(X_train, y_train)))

# Print the test set accuracy for the new model
print("Test set accuracy: {:.3f}".format(logreg001.score(X_test, y_test)))
