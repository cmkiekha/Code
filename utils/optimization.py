from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

import json

class Optimizer:
    def __init__(self, estimator, estimator_name, scoring="accuracy"):
        self.estimator = estimator
        self.estimator_name = estimator_name

        with open("model_grids.json", "r") as f:
            self.model_grids = json.load(f)
            
        self.param_grid = self.get_grid(estimator_name)
        self.scoring = scoring

    def grid_search(self, X_train, y_train, cv=5):
        grid_search_object = GridSearchCV(estimator=self.estimator, param_grid=self.param_grid, scoring=self.scoring, cv=cv)
        grid_search_object.fit(X_train, y_train)
        return grid_search_object.best_estimator_

    def random_search(self, X_train, y_train, n_iter=10, cv=5):
        random_search_object = RandomizedSearchCV(estimator=self.estimator, param_distributions=self.param_grid, scoring=self.scoring, cv=cv, n_iter=n_iter)
        random_search_object.fit(X_train, y_train)
        return random_search_object.best_estimator_
    
    def get_grid(self, model_name):
        return self.model_grids["models"][model_name]["param_grid"]
