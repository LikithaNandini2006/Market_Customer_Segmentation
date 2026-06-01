import numpy as np
from sklearn.cluster import KMeans

def find_optimal_clusters(data, max_clusters=10):
    """Return the KMeans inertia values for k = 1..max_clusters."""
    if max_clusters < 1:
        raise ValueError("max_clusters must be at least 1")

    data_arr = np.asarray(data, dtype=float)
    inertia = []

    for k in range(1, max_clusters + 1):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )
        model.fit(data_arr)
        inertia.append(float(model.inertia_))

    return inertia


def perform_clustering(data, n_clusters=5):
    """Fit KMeans and return cluster labels."""
    if n_clusters < 1:
        raise ValueError("n_clusters must be at least 1")

    data_arr = np.asarray(data, dtype=float)
    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    labels = model.fit_predict(data_arr)

    return labels
