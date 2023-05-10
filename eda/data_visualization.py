import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class DataVisualizer:
    '''
    Basic class for Data Visualization.
    '''
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def plot_correlation_matrix(self, outpath):
        """
        Plot correlation matrix of the data.
        """
        plt.figure(figsize=(10, 8))

        # Only look at numeric features in the numpy array (features with more than 2 unique values)
        df = pd.DataFrame(self.X)

        df = df.dropna()
        df = df.astype(float)

        # Linear correlation matrix, vmin=-1, vmax=1 is because correlation is measured in range -1, 1
        numerical_columns = df.select_dtypes(include=['float'])
        sns.heatmap(numerical_columns.corr(), vmin=-1, vmax=1, square=True, cmap="RdBu_r")
        plt.savefig(outpath)

    def plot_feature_distributions(self, outpath):
        pass
        # plt.figure(figsize=(10, 8))
        
        # names = pd.DataFrame(self.X)

        # n = len(names)
        # m = int(np.sqrt(n))

        # for i, feature in enumerate(names):
        #     plt.subplot(m, m, i + 1)
        #     sns.histplot(self.X[:, i])
        #     plt.title(feature)
        #     plt.ylabel('Count')
        #     plt.xlabel('Value')

        # plt.savefig(outpath)

    def plot_missingness(self, outpath):
        data = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

        missing_data = data.apply(lambda x: (x == ' ').sum())
        missing_data_percent = missing_data / len(data) * 100

        plt.figure(figsize=(10, 8))
        plt.bar(x = missing_data_percent.index, height=missing_data_percent.values)
        plt.xticks(rotation=90)
        plt.ylabel("Percentage of Missing Data")
        plt.title("Amount of Missing Data by Feature")
        plt.savefig(outpath)
