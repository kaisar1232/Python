import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split  # Added for splitting data
from sklearn.metrics import accuracy_score  # Added for calculating accuracy

# get the data
data = pd.read_csv('PlayPredictor.csv')
print(data)

# Preprocess the data

weather = data.Whether
Temperature = data.Temperature
play = data.Play

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
weather_encoded = le.fit_transform(weather)
print(weather_encoded)

# Converting string labels into numbers
temp_encoded = le.fit_transform(Temperature)
label = le.fit_transform(play)

# Combining weather and temp into a single list of tuples
features = list(zip(weather_encoded, temp_encoded))

# Step 1: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

# Step 3: Train Data
model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
model.fit(X_train, y_train)

# Step 4: Test data
predicted = model.predict(X_test)

# Step 5: Calculate accuracy
accuracy = accuracy_score(y_test, predicted)

print("Predicted labels:", predicted)
print("Accuracy:", accuracy)

