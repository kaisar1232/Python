import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def MarvellouskMean():
    print("__________________")
    
    # Set three centers, the model should predict similar results
    center_1 = np.array([1, 1])
    print(center_1)
    print("___________________")
    center_2 = np.array([5, 5])
    print(center_2)
    center_3 = np.array([8, 1])
    print(center_3)

    # Generate random data and center it to the three centers
    data_1 = np.random.randn(7, 2) + center_1
    print("Elements of the first cluster with size " + str(len(data_1)))
    print(data_1)
    
    data_2 = np.random.randn(7, 2) + center_2
    print("Elements of the second cluster with size " + str(len(data_2)))
    print(data_2)
    
    data_3 = np.random.randn(7, 2) + center_3
    print("Elements of the third cluster with size " + str(len(data_3)))
    print(data_3)

    data = np.concatenate((data_1, data_2, data_3), axis=0)
    print("Size of complete data set " + str(len(data)))
    print(data)

    plt.scatter(data[:,0], data[:,1], s=7)
    plt.title('Input Dataset')
    plt.show()

    # Number of clusters
    k = 3

    # Number of training data
    n = data.shape[0]
    print("Total number of elements are", n)

    # Number of features in the data
    c = data.shape[1]
    print("Total number of features are", c)

    # Generate random centers, here we use sigma and mean to ensure it
    mean = np.mean(data, axis=0)
    print("Value of mean", mean)

    # Calculate standard deviation
    std = np.std(data, axis=0)
    print("Value of std", std)

    centers = np.random.randn(k, c) * std + mean
    print("Random points are", centers)

    plt.scatter(data[:,0], data[:,1], c='r', s=7)
    plt.scatter(centers[:,0], centers[:,1], marker='o', c='g', s=150)
    plt.title(' Input Dataset with random centroids')
    plt.show()

    centers_old = np.zeros(centers.shape) # to store old centers
    centers_new = deepcopy(centers) # Store new centers

    print("Values of old centroids")
    print(centers_old)
    print("___________________")
    print("Values of new centroids")
    print(centers_new)

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("Initial distances are")
    print(distances)

    error = np.linalg.norm(centers_new - centers_old)
    print("value of error is ", error)

    while error != 0:
        print("value of error is ", error)

        # Measure the distance to every center
        print("Measure the distance to every center")

        for i in range(k):
            print("Iteration number ", i)

        # Assign all training data to the closest center
        clusters = np.argmin(distances, axis=1)
        centers_old = deepcopy(centers_new)

        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i], axis=0)

        error = np.linalg.norm(centers_new - centers_old)

    # End of while
    centers_new

    # Plot the data and the centers generated as random
    plt.scatter(data[:,0], data[:,1], s=7)
    plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)
    plt.title(' Final data with Centroid')
    plt.show()

def main():
    
    print("Unsupervised Machine Learning")
    print("Clustering using K Mean Algorithm")
    MarvellouskMean()

if __name__ == "__main__":
    main()
