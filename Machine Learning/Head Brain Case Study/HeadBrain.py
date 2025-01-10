import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the function to perform linear regression
def MarvellousHeadBrainPredictor():
    # Load the data
    data = pd.read_csv("MarvellousHeadBrain.csv")
    print("Size of the data set:", data.shape)
    
    # Extract the features and target variable
    X = data['Head Size(cm^3)'].values  # Corrected syntax
    Y = data['Brain Weight(grams)'].values  # Corrected syntax
    
    # Least Squares method
    mean_x = np.mean(X)  # Corrected syntax
    mean_y = np.mean(Y)  # Corrected syntax
    n = len(X)
    numerator = 0
    denominator = 0
    
    # Calculate the slope (m) and y-intercept (c) for the regression line
    # Equation of line is y = mx + c
    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denominator += (X[i] - mean_x) ** 2
    
    m = numerator / denominator
    c = mean_y - (m * mean_x)
    
    # Print the slope and y-intercept of the regression line
    print("Slope of the Regression line is:", m)
    print("Y-intercept of the Regression line is:", c)
    
    # Find the range for plotting the line
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100

    # Generate points for the regression line
    x = np.linspace(min_x, max_x, n)
    y = c + m * x

    # Display the plotting of the points
    plt.plot(x, y, color="#586970", label='Regression Line')
    plt.scatter(X, Y, color='#ef5423', label='Scatter Plot')  # Corrected syntax
    
    plt.xlabel('Head size in cm^3')
    plt.ylabel('Brain weight in grams')
    plt.legend()
    plt.show()

    # Find out the goodness of fit - R Square
    ss_t = 0
    ss_r = 0
    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y) ** 2
        ss_r += (Y[i] - y_pred) ** 2

    r2 = 1 - (ss_r / ss_t)
    print("R-squared (Goodness of Fit):", r2)

# Define the main function
def main():
    print("Marvellous Infosystems by Piyush Khaimar")
    print("Supervised Machine Learning")
    print("Linear Regression on Head and Brain size dataset")
    MarvellousHeadBrainPredictor()

# Call the main function
if __name__ == "__main__":
    main()
