import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Function to load the dataset
def load_iris_dataset(file_path='iris.csv'):
    dataset = pd.read_csv(file_path)
    x = dataset.iloc[:, [0, 1, 2, 3]].values
    return x

# Function to find the optimum number of clusters using the elbow method
def find_optimal_clusters(x, max_clusters=10):
    wcss = []
    for i in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
    return wcss

# Function to perform K-Means clustering and visualize the results
def kmeans_clustering(x, num_clusters=3):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(x)

    # Visualize the clusters
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Iris-setosa')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='blue', label='Iris-versicolour')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')

    # Plot the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label='Centroids')
    plt.legend()
    plt.show()

# Main program
if __name__ == '__main__':
    x = load_iris_dataset()
    
    # Find the optimal number of clusters using the elbow method
    wcss = find_optimal_clusters(x)
    
    # Plot the elbow method results
    plt.plot(range(1, len(wcss) + 1), wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')  # within cluster sum of squares
    plt.show()
    
    # Perform K-Means clustering with a chosen number of clusters (e.g., 3)
    kmeans_clustering(x, num_clusters=3)