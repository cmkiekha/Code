config = {
    "logistic_regression": {
        "param_grid": {
            "multi_class": "ovr",
            "max_iter": 1500,
        }
    },
    "xgboost": {
        "param_grid": {
            "tree_method": "exact", 
            "subsample": 0.60,  
            "reg_lambda": 0.15, 
            "n_estimators": 250,
            "min_child_weight": 0, 
            "max_depth": 9,
            "gamma": 1,
            "alpha": 0.01,
            "eta": 0.005,
            "colsample_bytree": 0.5,
            "colsample_bynode": 0.7,
            "colsample_bylevel": 0.5
        }
    },
    "random_forest": {
        "param_grid": {
            "n_estimators": 1000,
            "min_samples_split": 2,
            "min_samples_leaf": 1,
            "max_depth": 10,
            "max_features": "log2",
            "criterion": "gini",
            "bootstrap": True
        }
    },
    "knn": {
        "param_grid": {
            "p": 1,
            "n_neighbors": 7,
            "leaf_size": 40,
            "weights": "distance",
            "metric": "manhattan",
            "algorithm": "ball_tree"
        }
    },
    "mlp": {
        "param_grid": {
            "hidden_layer_sizes": (125,125),
            "activation": "relu",
            "solver": "adam",
            "alpha": 0.001,
            "max_iter": 5000,
            "learning_rate": "adaptive", 
            "random_state": 1234
        }
    }
}

def get_churn_grid(model_name):
    return config[model_name]["param_grid"]
