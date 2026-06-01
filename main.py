import os

os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")

from src.clustering import find_optimal_clusters, perform_clustering
from src.data_preprocessing import load_data, preprocess_data
from src.pca_analysis import apply_pca
from src.rfm_analysis import create_rfm_features
from src.visualization import plot_clusters, plot_elbow_method, plot_pca_clusters

print("Loading Dataset...")

os.makedirs("outputs", exist_ok=True)

data_file = "dataset/Mall_Customers.csv" if os.path.exists("dataset/Mall_Customers.csv") else "Mall_Customers.csv"
if not os.path.exists(data_file):
    raise FileNotFoundError(f"Dataset file not found: {data_file}")

df = load_data(data_file)

df = preprocess_data(df)

print("Creating RFM Features...")

rfm = create_rfm_features(df)

print("Finding Optimal Clusters...")

inertia = find_optimal_clusters(rfm)

plot_elbow_method(inertia)

print("Applying PCA...")

pca_data = apply_pca(rfm)

print("Performing Clustering...")

labels = perform_clustering(rfm)

rfm["Cluster"] = labels

plot_clusters(
    rfm[['Recency','Frequency']].values,
    labels
)

plot_pca_clusters(
    pca_data,
    labels
)

cluster_report = rfm.groupby("Cluster").mean()

cluster_report.to_csv(
    "outputs/cluster_report.csv"
)

print("\nProject Completed Successfully")
