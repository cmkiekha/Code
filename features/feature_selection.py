# TODO: Update code

def plot_feature_importances(X, y)
    rf=RandomForestClassifier(random_state = 42)
    rf.fit(data_telecom_encoded_X, data_telecom_encoded_y)
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]

    feature_names = [c for c in data_telecom_encoded_X.columns]
    plt.figure(figsize=(10,6))
    plt.bar(range(data_telecom_encoded_X.shape[1]),importances[indices])
    plt.xticks(range(data_telecom_encoded_X.shape[1]),feature_names)
    plt.xticks(rotation=90)
    plt.show()