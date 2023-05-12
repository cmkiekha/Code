import numpy as np
import pandas as pd
import scipy.stats as stats

from sklearn.metrics import confusion_matrix, mean_squared_error, r2_score, explained_variance_score, classification_report


class StatisticalAnalyzer:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
    
    def get_classification_report(self, custom_report=False):
        if custom_report:
            tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()

            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)
            accuracy = (tp + tn) / (tp + tn + fp + fn)

            return f"'Precision | Recall | F1 Score | Accuracy\n{precision} | {recall} | {f1_score} | {accuracy}'"
        else:
            return classification_report(self.y_true, self.y_pred)

    def get_regression_report(self):
        mse = mean_squared_error(self.y_true, self.y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_true, self.y_pred)
        evs = explained_variance_score(self.y_true, self.y_pred)

        return f"'MSE | RMSE | R2 | Explained Variance\n{mse} | {rmse} | {r2} | {evs}'"
