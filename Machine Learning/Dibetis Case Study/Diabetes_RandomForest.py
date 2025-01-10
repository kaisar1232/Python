import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter

# Ignore FutureWarnings
simplefilter(action='ignore', category=FutureWarning)

# Print information about the program
print("Marvellous Infosystems by Piyush Khairnar")
print("Diabetes predictor using Random Forest")

# Read the diabetes dataset
diabetes = pd.read_csv('diabetes.csv')

# Print column names
print("Columns of Dataset:")
print(diabetes.columns)

# Print the first 5 records
print("First 5 records of dataset:")
print(diabetes.head())

# Print the dimensions of the diabetes data
print("Dimension of diabetes data: {}".format(diabetes.shape))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

# Create and fit a RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=0)
rf.fit(X_train, y_train)

# Print accuracy on the training and test sets
print("Accuracy on training set: {:.3f}".format(rf.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(rf.score(X_test, y_test)))

# Create and fit another RandomForestClassifier with max_depth
rf1 = RandomForestClassifier(max_depth=3, n_estimators=100, random_state=0)
rf1.fit(X_train, y_train)

# Print accuracy on the training and test sets for the second model
print("Accuracy on training set: {:.3f}".format(rf1.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(rf1.score(X_test, y_test)))

# Define a function to plot feature importances
def plot_feature_importances(model, diabetes):
    plt.figure(figsize=(8, 6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    diabetes_features = [x for i, x in enumerate(diabetes.columns) if i != 8]
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()

# Plot feature importances for the first model
plot_feature_importances(rf, diabetes)
