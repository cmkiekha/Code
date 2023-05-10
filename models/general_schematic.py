import numpy as np
import sklearn
import matplotlib
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score


# Module for Hyperparameter Optimization
# What functions / utilities should this have?
# 1.) Function that takes in a model and a grid, and returns best hyperparams
# 2.) Function that takes in a list of models, and a list of grids, and returns the best model
# 3.) Main function which actually runs the model selection


def do_grid_search(model, hp_grid):
    gridsearch = GridSearchCV(model, hp_grid, refit=True, scoring=f1_score)
                              
    best_model = gridsearch.best_estimator_
    best_hps = gridsearch.best_params_
    best_score = gridsearch.best_score_
    
    # todo: save the output of gridsearch to a csv
    
    return best_model, best_hps, best_score


def model_selection(model_list, hp_grid_list):
    # model_list = [LinearRegression, NeuralNetwork, XGBoost]
    # hp_grid_list = [hp_lr, hp_nn, hp_xgb]
    # e.g. hp_lr = {'lr': 0.01, 'C': 1.0}
    
    
    best_model, best_hps, best_score = None, None, np.inf
    for model, hp_grid in zip(model_list, hp_grid_list):
        best_model_gs, best_hps_gs, best_score_gs = do_grid_search(model, hp_grid)
        
        if best_score_gs < best_score:
            best_model = best_model_gs
            best_hps = best_hps_gs
            best_score = best_score_gs
            
    return best_model, best_hps, best_score


def run_script():
    model_list = [LinearRegression, NeuralNetwork, XGboost]
    
    hp_lr = {'lr': [0.01, 0.05],
             'C': [1.0, 2.0]
    }
    
    hp_nn = {'hidden_units': [64],
             'depth': [4, 8, 12]
    }
    
    hp_xgb = {'n_estimators': [50]        
    }
    
    hp_grid_list = [hp_lr, hp_nn, hp_xgb]
    
    
    best_model, best_hps, best_score = model_selection(model_list, hp_grid_list)
    
    return best_model, best_hps, best_score
