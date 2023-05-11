echo "------------- Churn Dataset -------------" > outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Logistic Regression" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection borutashap --model logistic_regression >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Random Forest" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection borutashap --model random_forest >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "XGBoost" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection borutashap --model xgboost >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "kNN Classifier" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection borutashap --model knn >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Multi-Layer Perceptron" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection borutashap --model mlp >> outputs/borutashap_data.txt

echo "---------- Engineering Dataset ----------" >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Linear Regression" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model linear_regression >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Random Forest" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model random_forest >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Elastic Net" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model elastic_net >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Ridge" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model ridge >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Lasso" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model lasso >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "XGBoost" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model xgboost >> outputs/borutashap_data.txt

echo "" >> outputs/borutashap_data.txt
echo "Multi-Layer Perceptron" >> outputs/borutashap_data.txt
echo "" >> outputs/borutashap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model mlp >> outputs/borutashap_data.txt