'''In this application we create our own algorithm for classified machine learning.
• We create our own K Nearest Neighbour algorithm.
• For user defined algorithm we design one class named as MarvellousKNN. • This class contains 3 methods as fit, predict, closest method.
• There is one naked method euc() which calculate distance between two points using
Euclidean distance algorithm. fit() method initialises training data and its targets inside class.
• predict() method creates one array as prediction which stores shortest distance
between all test data and training data elements.
• predict() method calls closest method which returns the shortest distance'''


from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a, b):
    return distance.euclidean(a, b)

class MarvellousKNN():
    def fit(self, TrainingData, TrainingTarget):
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget

    def predict(self, TestData):
        predictions = []
        for row in TestData:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        bestdistance = euc(row, self.TrainingData[0])
        bestindex = 0
        for i in range(1, len(self.TrainingData)):
            dist = euc(row, self.TrainingData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i
        return self.TrainingTarget[bestindex]

def MarvellousKNeighbor():
    border = "-" * 50

    iris = load_iris()
    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID: %d, Label: %s, Feature: %s" % (i, iris.target[i], iris.data[i]))
    print("Size of Actual data set %d" % (i + 1))

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    print(border)
    print("Training data set")
    print(border)

    for i in range(len(data_train)):
        print("ID: %d, Label: %s, Feature: %s" % (i, target_train[i], data_train[i]))
    print("Size of Training data set %d" % (i + 1))

    print(border)
    print("Test data set")
    print(border)

    for i in range(len(data_test)):
        print("ID: %d, Label: %s, Feature: %s" % (i, target_test[i], data_test[i]))
    print("Size of Test data set %d" % (i + 1))

    print(border)

    classifier = MarvellousKNN()
    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():
    Accuracy = MarvellousKNeighbor()
    print("Accuracy of classification algorithm with K Neighbor classifier is", Accuracy * 100, "%")

if __name__ == "__main__":
    main()
