from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import json  # config is a file name; dictionaries are pretty con
# json is a built in library to help process json files.  the actual file in downloaded on line 10

class Optimizer:  # for HPO; class takes in estimator and runs grid search on it
    def __init__(self, estimator, estimator_name, scoring='accuracy'):  # self could be object or it; every member function has to have self as member parameter
        self.estimator = estimator # actual model
        self.estimator_name = estimator_name  # what every is in config.json file

        with open('config.json', 'r') as f:  # open this file; open mode is r - read
            self.model_grids = json.load(f)  # creating variable that named model_grids and that loads json from the file into a dictionary; thus model_grids is now a dic
            
        self.param_grid = self.get_grid(estimator_name)  # call whatever grid you want that is stored in config json file
        self.scoring = scoring

    def grid_search(self, X_train, y_train, cv=5):
        grid_search_object = GridSearchCV(estimator=self.estimator, param_grid=self.param_grid, scoring=self.scoring, cv=cv)  # var name storing value of variable which is object of whatever comes back from GridSearch
        grid_search_object.fit(X_train, y_train)
        return grid_search_object.best_estimator_

    def random_search(self, X_train, y_train, n_iter=10, cv=5):
        random_search_object = RandomizedSearchCV(estimator=self.estimator, param_distributions=self.param_grid, scoring=self.scoring, cv=cv, n_iter=n_iter)
        random_search_object.fit(X_train, y_train)
        return random_search_object.best_estimator_
    
    def get_grid(self, model_name):
        return self.model_grids['models'][model_name]['param_grid']  # models-> model name -> function returns the parameter grid for the designated model
