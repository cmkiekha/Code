from sklearn.ensemble import RandomForestClassifier

import numpy as np
import matplotlib.pyplot as plt


def plot_feature_importances(X, y):
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X, y)

    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]

    # Extract feature names from DataFrame
    feature_names = [c for c in X.columns]

    plt.figure(figsize=(10, 6))
    plt.bar(range(X.shape[1]), importances[indices])
    plt.xticks(range(X.shape[1]), feature_names)
    plt.xticks(rotation=90)
    plt.show()
