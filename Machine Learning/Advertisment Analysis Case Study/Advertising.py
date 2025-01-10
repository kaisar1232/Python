import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Get the data
data = pd.read_csv('Advertising.csv')

# Clean, prepare, manipulate data
X = data[['TV', 'radio', 'newspaper']]
y = data['sales']

# Data splitting
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()

# Train the model using the training set
model.fit(x_train, y_train)

# Test the model
y_pred = model.predict(x_test)
print(y_pred)

# Calculate regression metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)
