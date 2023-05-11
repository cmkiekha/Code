config = {
    "linear_regression": {
        "param_grid": {}
    },
    "xgboost": {
        "param_grid": {
            "subsample": 0.6,
            "reg_lambda": 1,
            "reg_alpha": 0,
            "n_estimators": 1000,
            "min_child_weight": 3,
            "max_depth": 5,
            "learning_rate": 0.2,
            "gamma": 0.5,
            "colsample_bytree": 0.8,
            "eval_metric": "mae",
            "objective": "reg:squarederror"
        }
    },
    "ridge": {
        "param_grid": {
            "tol": 0.02,
            "solver": "sparse_cg",
            "max_iter": 5000,
            "fit_intercept": True,
            "alpha": 0.1
            }
        },
    "lasso": {
        "param_grid": {
            "tol": 0.05,
            "selection": "random",
            "max_iter": 600,
            "fit_intercept": True,
            "alpha": 0.05
        }
    },
    "elastic_net": {
        "param_grid": {
            "tol": 0.1,
            "selection": "random",
            "max_iter": 5000,
            "l1_ratio": 1.0,
            "fit_intercept": True,
            "alpha": 0.34
        }
    },
    "mlp": {
        "param_grid": {
            "hidden_layer_sizes": (100,),
            "max_iter": 1000,
            "activation": "relu",
            "solver": "adam",
            "alpha": 0.001,
            "learning_rate": "adaptive"
        }
    }
}

def get_print_grid(model_name):
    return config[model_name]["param_grid"]
