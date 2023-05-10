echo "------------- Churn Dataset -------------" > output.txt

echo "" >> output.txt
echo "Logistic Regression" >> output.txt
echo "" >> output.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model logistic_regression >> output.txt

echo "" >> output.txt
echo "Random Forest" >> output.txt
echo "" >> output.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model random_forest >> output.txt

echo "" >> output.txt
echo "XGBoost" >> output.txt
echo "" >> output.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model xgboost >> output.txt

echo "" >> output.txt
echo "kNN Classifier" >> output.txt
echo "" >> output.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model knn >> output.txt

echo "" >> output.txt
echo "Multi-Layer Perceptron" >> output.txt
echo "" >> output.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --model mlp >> output.txt

echo "---------- Engineering Dataset ----------" >> output.txt

echo "" >> output.txt
echo "Linear Regression" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model linear_regression >> output.txt

echo "" >> output.txt
echo "Random Forest" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model random_forest >> output.txt

echo "" >> output.txt
echo "Elastic Net" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model elastic_net >> output.txt

echo "" >> output.txt
echo "Ridge" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model ridge >> output.txt

echo "" >> output.txt
echo "Lasso" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model lasso >> output.txt

echo "" >> output.txt
echo "XGBoost" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model xgboost >> output.txt

echo "" >> output.txt
echo "Multi-Layer Perceptron" >> output.txt
echo "" >> output.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model mlp >> output.txt