import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Generate synthetic data
df = pd.read_csv("./SnowDepth_1.csv")
X = df["snowdepth"]
X = StandardScaler().fit_transform(X)

# Determine the optimal number of clusters using the elbow method
wcss = []  # Within-cluster sum of squares
silhouette_scores = []

for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))
# Plot the elbow method results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(range(2, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

# Plot the silhouette scores
plt.subplot(1, 2, 2)
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Score')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')

plt.show()

# Choose the optimal number of clusters (based on the elbow or silhouette method)
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(X)

# Detect outliers based on distance from the cluster center
distances = kmeans.transform(X)
min_distances = np.min(distances, axis=1)
threshold = np.percentile(min_distances, 95)  # Set a threshold for outlier detection
outliers = X[min_distances > threshold]

# Visualize the clusters and outliers
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(outliers[:, 0], outliers[:, 1], c='red', marker='x', s=100, label='Outliers')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='blue', marker='D', s=100, label='Centroids')
plt.title(f'K-Means Clustering (k={optimal_clusters})')
plt.legend()
plt.show()