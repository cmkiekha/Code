import argparse
import os

from utils.data_loader import ChurnDataLoader, EngineeringDataLoader

from eda.data_visualization import DataVisualizer
from eda.statistical_analysis import StatisticalAnalyzer

from models.parametric import *
from models.non_parametric import *

from hp_config.churn import get_churn_grid
from hp_config.print import get_print_grid


def main(args):
    # 1a. Data Preprocessing
    if args.data == 'churn':
        data_loader = ChurnDataLoader(args.data_path, target_column='Churn', test_size=0.2, imb_strat='smote')
    elif args.data == 'engineering':
        data_loader = EngineeringDataLoader(args.data_path, target_column='tension_strength', test_size=0.2)

    print(f'The {args.data} data loaded successfully.')

    # 1b. Data Exploration
    if args.eda:
        if args.data == 'churn':
            visualizer_before_preprocessing = DataVisualizer(data_loader.X_preproc, data_loader.y_preproc)
        visualizer_after_preprocessing = DataVisualizer(data_loader.X, data_loader.y)

        # 1b(i). Correlation Matrix
        visualizer_after_preprocessing.plot_correlation_matrix(os.path.join(args.eda_figures, f'correlation_matrix_{args.data}.JPG'))

        # 1b(ii). Distribution Plot
        visualizer_after_preprocessing.plot_feature_distributions(os.path.join(args.eda_figures, f'distributions_{args.data}.JPG'))

        if args.data == 'churn':
            # 1b(iii). Imbalance Plot
            visualizer_before_preprocessing.plot_missingness(os.path.join(args.eda_figures, f'missingness_{args.data}.JPG'))

    # 2. Feature Selection
    top_feats = ...
    if args.selection is None or args.data == 'engineering':
        pass
    elif args.selection == 'rf':
        top_feats = ['MonthlyCharges', 'TotalCharges', 'Tenure']
        data_loader.X_train, data_loader.X_test = data_loader.X_train[top_feats], data_loader.X_test[top_feats]
    elif args.selection == 'shap':
        top_feats = ['Tenure', 'InternetService', 'TechSupport', 'OnlineSecurity', 'PaymentMethod']
        data_loader.X_train, data_loader.X_test = data_loader.X_train[top_feats], data_loader.X_test[top_feats]
    elif args.selection == 'borutashap':
        top_feats = ['Contract', 'InternetService', 'MonthlyCharges', 'Tenure', 'TotalCharges', 'PaymentMethod']
        data_loader.X_train, data_loader.X_test = data_loader.X_train[top_feats], data_loader.X_test[top_feats]
    else:
        raise ValueError("Error: Given feature selection method is invalid.")

    # 3a. Model Initialization
    current_model = ...
    param_grid = ...

    if args.no_grid:
        try:
            if args.data == 'churn':
                param_grid = get_churn_grid(args.model)
            else:
                param_grid = get_print_grid(args.model)
        except:
            print("Warning: No parameter grid found. Using default parameters.")
            param_grid = {}
    else:
        print("Warning: No parameter grid found. Using default parameters.")
        param_grid = {}

    # Classification (Churn)
    if args.data == 'churn':
        if args.model == 'logistic_regression':
            current_model = ParametricClassifier(model_type='logistic_regression', params=param_grid)
        elif args.model == 'random_forest':
            current_model = NonparametricClassifier(model_type='random_forest', params=param_grid)  
        elif args.model == 'xgboost':
            current_model = NonparametricClassifier(model_type='xgboost', params=param_grid)
        elif args.model == 'knn':
            current_model = NonparametricClassifier(model_type='knn', params=param_grid)
        elif args.model == 'mlp':
            current_model = NonparametricClassifier(model_type='mlp', params=param_grid)

    # Regression (3D Printing)
    else:
        if args.model == 'linear_regression':
            current_model = ParametricRegressor(model_type='linear_regression', params=param_grid)
        elif args.model == 'elastic_net':
            current_model = ParametricRegressor(model_type='elastic_net', params=param_grid)
        elif args.model == 'ridge':
            current_model = ParametricRegressor(model_type='ridge', params=param_grid)
        elif args.model == 'lasso':
            current_model = ParametricRegressor(model_type='lasso', params=param_grid)
        elif args.model == 'random_forest':
            current_model = NonparametricRegressor(model_type='random_forest', params=param_grid)  
        elif args.model == 'xgboost':
            current_model = NonparametricRegressor(model_type='xgboost', params=param_grid)
        elif args.model == 'mlp':
            current_model = NonparametricRegressor(model_type='mlp', params=param_grid)

    # 3b. Model Training
    current_model.model.fit(data_loader.X_train, data_loader.y_train)

    # 3c. Model Evaluation
    y_pred = current_model.model.predict(data_loader.X_test)
    analyzer = StatisticalAnalyzer(data_loader.y_test, y_pred)

    if args.data == 'churn':
        print(analyzer.get_classification_report())
    else:
        print(analyzer.get_regression_report())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--data', type=str, choices=['churn', 'engineering'], default='churn', 
                        help='What type of dataset to use')
    parser.add_argument('--data_path', type=str, default='./data/WA_Fn-UseC_-Telco-Customer-Churn.csv',
                        help='Path to the dataset')
    parser.add_argument('--selection', type=str, default=None,
                        help='Feature selection approach. Default to None.')
    parser.add_argument('--eda', action='store_true', default=True,
                        help='Whether to perform exploratory data analysis')
    parser.add_argument('--no_grid', type=bool, default=False,
                        help='Whether to use the custom param grids from config or not.')
    parser.add_argument('--eda_figures', type=str, default='./figures',
                        help='Path to save the figures generated from EDA')
    parser.add_argument('--model', type=str, default='xgboost',
                        help='What type of model to use (parametric or non-parametric)')
    args = parser.parse_args()

    main(args)
