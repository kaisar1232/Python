import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

print("Feature names of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

# Indices of removed elements
test_index = [1,51,101]

# Training data with removed elements
train_target = np.delete(iris.target,test_index)
train_data = np.delete(iris.data,test_index,axis=0)

# Testing data for testing on trainning data
test_target = iris.target[test_index]   # A B C
test_data = iris.data[test_index]       # 1234   1234   1234

# form decision tree classifier
classifier = tree.DecisionTreeClassifier()

# Apply training data to form tree
classifier.fit(train_data,train_target)

print("Values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))
