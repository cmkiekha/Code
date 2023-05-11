echo "------------- Churn Dataset -------------" > outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Logistic Regression" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model logistic_regression >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Random Forest" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model random_forest >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "XGBoost" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model xgboost >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "kNN Classifier" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model knn >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Multi-Layer Perceptron" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model mlp >> outputs/full_data.txt

echo "---------- Engineering Dataset ----------" >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Linear Regression" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model linear_regression >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Random Forest" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model random_forest >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Elastic Net" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model elastic_net >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Ridge" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model ridge >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Lasso" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model lasso >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "XGBoost" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model xgboost >> outputs/full_data.txt

echo "" >> outputs/full_data.txt
echo "Multi-Layer Perceptron" >> outputs/full_data.txt
echo "" >> outputs/full_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model mlp >> outputs/full_data.txt