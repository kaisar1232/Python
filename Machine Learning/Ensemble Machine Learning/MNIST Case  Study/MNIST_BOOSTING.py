import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# Load the data from 'mnist.csv'
data = pd.read_csv('mnist.csv')

# Separate features and labels
df_x = data.iloc[:, 1:]  # Features
df_y = data.iloc[:, 0]  # Labels

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

# Create an AdaBoostClassifier with DecisionTreeClassifier as base estimator
adb = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=100, learning_rate=1)

# Fit the AdaBoost classifier to the training data
adb.fit(x_train, y_train)

# Evaluate the classifier's performance
testing_accuracy = adb.score(x_test, y_test) * 100
training_accuracy = adb.score(x_train, y_train) * 100

print("Testing accuracy using AdaBoost classifier: ", testing_accuracy)
print("Training accuracy using AdaBoost classifier: ", training_accuracy)
