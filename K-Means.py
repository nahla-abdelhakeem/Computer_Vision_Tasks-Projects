
import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [1, 2], [2, 1], [2, 3],
    [8, 8], [9, 8], [8, 9],
    [4, 7], [5, 8], [5, 6]
])

K = 3


centroids = np.array([[1, 2], [8, 8], [4, 7]])

for i in range(10):

    clusters = [[], [], []]

    for point in points:
        distances = []

        for center in centroids:
            distance = np.linalg.norm(point - center)
            distances.append(distance)

        cluster = np.argmin(distances)
        clusters[cluster].append(point)

    for j in range(K):
        centroids[j] = np.mean(clusters[j], axis=0)

for i in range(K):
    cluster_points = np.array(clusters[i])
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i+1}")

plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='*', s=100, label='Centroids')

plt.legend()
plt.title("K-Means Clustering")
plt.show()
