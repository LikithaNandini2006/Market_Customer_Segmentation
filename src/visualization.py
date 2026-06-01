import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

def plot_elbow_method(inertia):

    plt.figure(figsize=(8,5))

    plt.plot(range(1, len(inertia) + 1), inertia, marker='o')

    plt.xlabel("Number of Clusters")
    plt.ylabel("Inertia")

    plt.title("Elbow Method")

    plt.savefig("outputs/elbow_method.png")

    plt.close()


def plot_clusters(data, labels):

    plt.figure(figsize=(8,6))

    plt.scatter(
        data[:,0],
        data[:,1],
        c=labels
    )

    plt.title("Customer Segments")

    plt.savefig("outputs/customer_clusters.png")

    plt.close()


def plot_pca_clusters(pca_data, labels):

    plt.figure(figsize=(8,6))

    plt.scatter(
        pca_data[:,0],
        pca_data[:,1],
        c=labels
    )

    plt.title("PCA Customer Segmentation")

    plt.savefig("outputs/pca_clusters.png")

    plt.close()
