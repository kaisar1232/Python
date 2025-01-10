from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 70% training and 30% test

# Create an AdaBoost classifier object
abc = AdaBoostClassifier(n_estimators=50, learning_rate=1)

# Train the AdaBoost classifier model
model = abc.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = model.predict(X_test)

# Calculate and print the accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
