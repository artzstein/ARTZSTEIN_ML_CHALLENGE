import numpy as np 
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression 
from sklearn.cluster import KMeans 

X, y = make_classification(n_samples=300, n_features=5, random_state=42)

supervised_model = LogisticRegression().fit(X, y)
print("Supervised accuracy:", supervised_model.score(X, y))

unsupervised_model = KMeans(n_clusters=2, n_init=10, random_state=42).fit(X)
print("Unsupervised cluster asignments (first 10):", unsupervised_model.labels_[:10])
from sklearn.metrics import adjusted_rand_score
print("Alignment with true labels (ARI):", adjusted_rand_score(y, unsupervised_model.labels_))
