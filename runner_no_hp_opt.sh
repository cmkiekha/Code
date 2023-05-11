echo "------------- Churn Dataset -------------" > outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Logistic Regression" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --no_grid True --model logistic_regression >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Random Forest" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --no_grid True --model random_forest >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "XGBoost" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --no_grid True --model xgboost >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "kNN Classifier" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --no_grid True --model knn >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Multi-Layer Perceptron" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --no_grid True --model mlp >> outputs/full_data_no_hp_opt.txt

echo "---------- Engineering Dataset ----------" >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Linear Regression" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model linear_regression >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Random Forest" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model random_forest >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Elastic Net" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model elastic_net >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Ridge" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model ridge >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Lasso" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model lasso >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "XGBoost" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model xgboost >> outputs/full_data_no_hp_opt.txt

echo "" >> outputs/full_data_no_hp_opt.txt
echo "Multi-Layer Perceptron" >> outputs/full_data_no_hp_opt.txt
echo "" >> outputs/full_data_no_hp_opt.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --no_grid True --model mlp >> outputs/full_data_no_hp_opt.txt