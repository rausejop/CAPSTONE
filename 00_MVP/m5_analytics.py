"""
Manager 5: Analytics & Clustering.
Groups processed intelligence into human-readable topics.
Uses Matplotlib for visual representation of geopolitical clusters.
"""
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np

class AnalyticsManager:
    def __init__(self, n_clusters: int = 3):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=self.n_clusters, n_init=10)

    def perform_clustering(self, embeddings: list):
        """
        Groups vectors into thematic clusters.
        Solves: Grouping massive datasets into human-readable topics.
        """
        if len(embeddings) < self.n_clusters:
            return [0] * len(embeddings)
        
        # Convert list to numpy array for processing
        data = np.array(embeddings)
        
        # Fit K-Means
        self.kmeans.fit(data)
        return self.kmeans.labels_

    def visualize_clusters(self, embeddings: list, labels: list, titles: list):
        """
        Requirement FUNC05: Matplotlib Cluster Map.
        Reduces dimensionality to 2D for human visualization via PCA.
        """
        data = np.array(embeddings)
        pca = PCA(n_components=2)
        reduced_data = pca.fit_transform(data)

        plt.figure(figsize=(10, 7))
        scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis')
        
        # Annotation of points (Optional: only first few to avoid noise)
        for i, title in enumerate(titles[:10]):
            plt.annotate(title[:20], (reduced_data[i, 0], reduced_data[i, 1]), fontsize=8)

        plt.title("Geopolitical Intelligence Clusters (USA-Iran Focus)")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.colorbar(scatter, label='Cluster ID')
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # Guardar en disco para no saturar la RAM con ventanas interactivas
        plt.savefig("./data/cluster_map.png")
        plt.close() # Liberar memoria inmediatamente
        print("Visualización generada en ./data/cluster_map.png")

# Ejemplo de integración
# labels = manager.perform_clustering(all_embeddings)
# manager.visualize_clusters(all_embeddings, labels, list_of_titles)