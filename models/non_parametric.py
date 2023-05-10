from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, SVR

import xgboost as xgb


class NonparametricClassifier:
    def __init__(self, model_type='random_forest', params={}) -> None:
        self.params = params
        if model_type == 'random_forest':
            self.model = RandomForestClassifier(**params, random_state=42)
        elif model_type == 'xgboost':
            self.model = xgb.XGBClassifier(**params, random_state=42)
        elif model_type == 'svm':
            self.model = SVC(**params, random_state=42)
        elif model_type == 'mlp':
            self.model = MLPClassifier(**params)
        elif model_type == 'knn':
            self.model = KNeighborsClassifier(**params)
        else:
            raise ValueError("Model type must be valid.")


class NonparametricRegressor:
    def __init__(self, model_type='random_forest', params={}) -> None:
        self.params = params
        if model_type == 'random_forest':
            self.model = RandomForestRegressor(**params, random_state=42)
        elif model_type == 'xgboost':
            self.model = xgb.XGBRegressor(**params, random_state=42)
        elif model_type == 'svm':
            self.model = SVR(**params, random_state=42)
        elif model_type == 'mlp':
            self.model = MLPRegressor(**params)
        else:
            raise ValueError("Model type must be valid.")
