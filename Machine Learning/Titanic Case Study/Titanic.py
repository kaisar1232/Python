# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def MarvellousTitanicLogistic():
    # Step 1: Load data
    titanic_data = pd.read_csv('MarvellousTitanicDataset.csv')

    print("First 5 entries from the loaded dataset:")
    print(titanic_data.head())
    print("Number of passengers: " + str(len(titanic_data)))

    # Step 2: Analyze data
    print("Visualization: Survived and non-survived passengers")
    sns.countplot(data=titanic_data, x="Survived").set_title("Survived and non-survived passengers")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on Gender")
    sns.countplot(data=titanic_data, x="Survived", hue="Sex").set_title("Survived and non-survived passengers based on Gender")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on the Passenger class")
    sns.countplot(data=titanic_data, x="Survived", hue="Pclass").set_title("Survived and non-survived passengers based on the Passenger class")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on Age")
    titanic_data["Age"].plot.hist().set_title("Survived and non-survived passengers based on Age")
    plt.show()

    print("Visualization: Survived and non-survived passengers based on the Fare")
    titanic_data["Fare"].plot.hist().set_title("Survived and non-survived passengers based on Fare")
    plt.show()

    # Step 3: Data Cleaning
    titanic_data.drop("zero", axis=1, inplace=True)  # Removed irrelevant column "zero"

    print("First 5 entries from the loaded dataset after removing the 'zero' column")
    print(titanic_data.head(5))
    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of Sex column after removing one field")
    Sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
    print(Sex.head(5))

    print("Values of Pclass column after removing one field")
    Pclass = pd.get_dummies(titanic_data["Pclass"], drop_first=True)
    print(Pclass.head(5))

    print("Values of the dataset after concatenating new columns")
    titanic_data = pd.concat([titanic_data, Sex, Pclass], axis=1)
    print(titanic_data.head(5))

    # Step 3: Data Cleaning (Updated)
    titanic_data.drop(["Sex", "SibSp", "Parch", "Embarked"], axis=1, inplace=True)

    x = titanic_data.drop("Survived", axis=1)
    y = titanic_data["Survived"]

    # Step 4: Data Training
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.5)

    logmodel = LogisticRegression()
    logmodel.fit(xtrain, ytrain)

    # Step 4: Data Testing
    prediction = logmodel.predict(xtest)

    # Step 5: Calculate Accuracy
    print("Classification report of Logistic Regression is:")
    print(classification_report(ytest, prediction))

    print("Confusion Matrix of Logistic Regression is:")
    print(confusion_matrix(ytest, prediction))

    print("Accuracy of Logistic Regression is:")
    print(accuracy_score(ytest, prediction))

def main():
    print("Marvellous Infosystems by Plyush Khairman")
    print("Supervised Machine Learning")
    print("Logistic Regression on Titanic dataset")
    MarvellousTitanicLogistic()

if __name__ == "__main__":
    main()
