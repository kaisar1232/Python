import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Print introductory messages
print("-- Application By Kaisar Attar --")
print("---- Diabetes predictor using Decision Tree -----")

# Read the diabetes dataset
diabetes = pd.read_csv('diabetes.csv')

# Print the columns of the dataset
print("Columns of Dataset:")
print(diabetes.columns)

# Print the first 5 records of the dataset
print("First 5 records of dataset:")
print(diabetes.head())

# Print the dimensions of the diabetes data
print("Dimension of diabetes data: {}".format(diabetes.shape))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state=66)

# Create a Decision Tree classifier and train it on the training data
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)

# Print the accuracy on the training and test sets
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

# Create a Decision Tree classifier with a specified max depth and train it
tree = DecisionTreeClassifier(max_depth=3, random_state=0)
tree.fit(X_train, y_train)

# Print the accuracy on the training and test sets
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

# Define a function to plot feature importances
def plot_feature_importances_diabetes(model):
    plt.figure(figsize=(8, 6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align='center')
    diabetes_features = [x for i, x in enumerate(diabetes.columns) if i != 8]
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()

# Plot feature importances for the Decision Tree model
plot_feature_importances_diabetes(tree)
