import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Print a message
print("Marvellous Infosystems by Piyush Khairnar")
print("Diabetes predictor using K Nearest neighbor")

# Load the diabetes dataset
diabetes = pd.read_csv('diabetes.csv')

# Print the columns of the dataset
print("Columns of Dataset")
print(diabetes.columns)

# Print the first 5 records of the dataset
print("First 5 records of dataset")
print(diabetes.head())

# Display the dimension of the diabetes data
print("Dimension of diabetes data: {}".format(diabetes.shape))

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    diabetes.loc[:, diabetes.columns != 'Outcome'],
    diabetes['Outcome'],
    stratify=diabetes['Outcome'],
    random_state=66
)

# Lists to store training and test accuracy
training_accuracy = []
test_accuracy = []

# Define the range of neighbors to try
neighbors_settings = range(1, 11)

# Iterate through different numbers of neighbors
for n_neighbors in neighbors_settings:
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    training_accuracy.append(knn.score(X_train, y_train))
    test_accuracy.append(knn.score(X_test, y_test))

# Plot the training and test accuracy
plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig("knn_compare_model.png")
plt.show()

# Create a KNN classifier with a specific number of neighbors (e.g., 9)
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)

# Print the accuracy of the K-NN classifier on the training and test sets
print('Accuracy of K-NN classifier on training set: {:.2f}'.format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'.format(knn.score(X_test, y_test)))
