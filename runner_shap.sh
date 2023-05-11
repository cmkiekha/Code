echo "------------- Churn Dataset -------------" > outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Logistic Regression" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection shap --model logistic_regression >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Random Forest" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection shap --model random_forest >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "XGBoost" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection shap --model xgboost >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "kNN Classifier" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection shap --model knn >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Multi-Layer Perceptron" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data churn --data_path ./data/WA_Fn-UseC_-Telco-Customer-Churn.csv --selection shap --model mlp >> outputs/shap_data.txt

echo "---------- Engineering Dataset ----------" >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Linear Regression" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model linear_regression >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Random Forest" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model random_forest >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Elastic Net" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model elastic_net >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Ridge" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model ridge >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Lasso" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model lasso >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "XGBoost" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model xgboost >> outputs/shap_data.txt

echo "" >> outputs/shap_data.txt
echo "Multi-Layer Perceptron" >> outputs/shap_data.txt
echo "" >> outputs/shap_data.txt

python main.py --data engineering --data_path http://apmonitor.com/pds/uploads/Main/manufacturing.txt --model mlp >> outputs/shap_data.txt