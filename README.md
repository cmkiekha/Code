# Guide

## Usage

```sh
usage: main.py [-h] [--data {churn,engineering}] [--data_path DATA_PATH] [--selection SELECTION] [--eda] [--no_grid NO_GRID] [--eda_figures EDA_FIGURES]
               [--model MODEL]

optional arguments:
  -h, --help            show this help message and exit
  --data {churn,engineering}
                        What type of dataset to use
  --data_path DATA_PATH
                        Path to the dataset
  --selection SELECTION
                        Feature selection approach. Default to None.
  --eda                 Whether to perform exploratory data analysis
  --no_grid NO_GRID     Whether to use the custom param grids from config or not.
  --eda_figures EDA_FIGURES
                        Path to save the figures generated from EDA
  --model MODEL         What type of model to use (parametric or non-parametric)
```

## Examples

### Classification

```sh
python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model MODEL
```

Model Options:
- logistic_regression
- random_forest
- xgboost
- knn
- mlp

### Regression

```sh
python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model MODEL
```

Model Options:
- linear_regression
- random_forest
- elastic_net
- ridge
- lasso
- xgboost
- mlp