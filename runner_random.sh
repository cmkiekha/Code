echo "------------- Churn Dataset -------------" > outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Logistic Regression" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection rf --model logistic_regression >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Random Forest" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection rf --model random_forest >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "XGBoost" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection rf --model xgboost >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "kNN Classifier" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection rf --model knn >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Multi-Layer Perceptron" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection rf --model mlp >> outputs/rf_data.txt

echo "---------- Engineering Dataset ----------" >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Linear Regression" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model linear_regression >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Random Forest" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model random_forest >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Elastic Net" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model elastic_net >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Ridge" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model ridge >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Lasso" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model lasso >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "XGBoost" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model xgboost >> outputs/rf_data.txt

echo "" >> outputs/rf_data.txt
echo "Multi-Layer Perceptron" >> outputs/rf_data.txt
echo "" >> outputs/rf_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model mlp >> outputs/rf_data.txt