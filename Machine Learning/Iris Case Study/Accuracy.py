'''•In this application we train iris data set with Decision Tree algorithm and K Nearest Neighbour algorithm.
• We divide iris data set into two equal parts as training data and test data.
• We apply training on training data and predict the result on test data.
• We calculate accuracy of both the algorithms by applying of test data.'''

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)
    
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(data_train, target_train)
    
    predictions = classifier.predict(data_test)
    Accuracy = accuracy_score(target_test, predictions)
    
    return Accuracy

def MarvellousCalculateAccuracyKNeighbor():
    iris = load_iris()
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    classifier = KNeighborsClassifier()
    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)
    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree classifier is", Accuracy * 100, "%")

    Accuracy = MarvellousCalculateAccuracyKNeighbor()
    print("Accuracy of classification algorithm with K Neighbor classifier is", Accuracy * 100, "%")

if __name__ == "__main__":
    main()
