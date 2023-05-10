from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso, ElasticNet


class ParametricClassifier:
    def __init__(self, model_type, params={}) -> None:
        self.params = params
        if model_type == 'logistic_regression':
            self.model = LogisticRegression(**params, random_state=42)
        else:
            raise ValueError("Model type must be valid.")


class ParametricRegressor:
    def __init__(self, model_type, params={}) -> None:
        self.params = params
        if model_type == 'linear_regression':
            self.model = LinearRegression(**params)
        elif model_type == 'ridge':
            self.model = Ridge(**params)
        elif model_type == 'lasso':
            self.model = Lasso(**params)
        elif model_type == 'elastic_net':
            self.model = ElasticNet(**params)
        else:
            raise ValueError("Model type must be valid.")
