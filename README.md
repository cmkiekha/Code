# Guide

## To run Classification on Churn

```sh
python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model INSERT_MODEL_NAME
```

Options:
- logistic_regression
- random_forest
- xgboost
- knn
- mlp

## To run Regression on Engineering

```sh
python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model INSERT_MODEL_NAME
```

Options:
- linear_regression
- random_forest
- elastic_net
- ridge
- lasso
- xgboost
- mlp
