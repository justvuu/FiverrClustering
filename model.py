import numpy as np

class KMeans:
    def __init__(self, n_clusters, max_iters=100, random_state=None):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = None

    def fit(self, X):
        np.random.seed(self.random_state)
        idx = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        self.centroids = X[idx]

        for _ in range(self.max_iters):
            labels = self._assign_labels(X)
            new_centroids = self._update_centroids(X, labels)
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

    def _assign_labels(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def _update_centroids(self, X, labels):
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])
        return new_centroids

    def predict(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def print_clusters(self, X, data):
        if self.centroids is None:
            print("K-Means has not been fitted yet.")
            return

        labels = self.predict(X)

        for i in range(self.n_clusters):
            print(f"--Centroid {i}: {self.centroids[i]}")
            cluster_indices = np.where(labels == i)[0]
            for idx in cluster_indices:
                print(data['username'][idx], end = " ")
            print("\n")

    def extract_features(self, X, cluster_labels):
        cluster_features = []
        for cluster_label in range(self.n_clusters):
            cluster_data = X[np.array(cluster_labels) == cluster_label]
            
            cluster_mean = np.mean(cluster_data, axis=0)
            cluster_std = np.std(cluster_data, axis=0)
            cluster_max = np.max(cluster_data, axis=0)
            cluster_min = np.min(cluster_data, axis=0)
            cluster_features.append({
                "Cluster Label": cluster_label,
                "Mean": cluster_mean,
                "Standard Deviation": cluster_std,
                "Max": cluster_max,
                "Min": cluster_min,
            })

        for cluster_feature in cluster_features:
            print(f"Cluster {cluster_feature['Cluster Label']} Features:")
            print(f"Mean: {cluster_feature['Mean']}")
            print(f"Standard Deviation: {cluster_feature['Standard Deviation']}")
            print(f"Max: {cluster_feature['Max']}")
            print(f"Min: {cluster_feature['Min']}")
            print()







