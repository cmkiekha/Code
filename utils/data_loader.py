# example of class instance implementation     
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import imblearn


def fix_imbalanced_data(strat, X_train, y_train):
    """
    Helper function that fixes imbalanced data using either oversampling, 
    undersampling, or SMOTE.
    """
    X_rebal, y_rebal = None, None
    # will rebalance so that minority and majority classes are equal
    if strat == 'over':
        oversampler = imblearn.over_sampling.RandomOverSampler(random_state=42) 
        X_rebal, y_rebal = oversampler.fit_resample(X_train, y_train)
    elif strat == 'under':
        undersampler = imblearn.under_sampling.RandomUnderSampler(random_state=42)
        X_rebal, y_rebal = undersampler.fit_resample(X_train, y_train)
    elif strat == 'smote':
        smote_oversampler = imblearn.over_sampling.SMOTE(k_neighbors=20, random_state=42)
        X_rebal, y_rebal = smote_oversampler.fit_resample(X_train, y_train) 
    return X_rebal, y_rebal


class DataLoader(object):
        """
            Class for data loading
            Parameters:
            - data_path: path to the csv file containing the data
            - target_column: response variable
            - test_size: percentage of size of test set
            - imb_strat: this indicates the strategy for oversampling, undersampling, or SMOTE
            - random_state: seed for reproducibility
        """
        def __init__(self, 
                     data_path, 
                     target_column, 
                     test_size=0.2, 
                     imb_strat=None,
                     random_state=42):
            self.data_path = data_path
            self.target_column = target_column
            self.test_size = test_size
            self.imb_strat = imb_strat
            self.random_state = random_state

            if self.imb_strat is not None:
                assert self.imb_strat in ['over', 'under', 'smote'], \
                    "Fixing imbalanced data strategy must be one of ('over', 'under', or 'smote')"

        def load_data(self):
            return pd.read_csv(self.data_path)
        
        def train_test_split(self):
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=self.test_size, random_state=self.random_state)

            print("-" * 50)
            print(f'The number of training samples is {len(X_train)}')
            print(f'The number of testing samples is {len(X_test)}')
            print("-" * 50)

            if self.imb_strat is not None:
                X_train, y_train = fix_imbalanced_data(self.imb_strat, X_train, y_train)
                print(f'The number of training samples after rebalancing is {len(X_train)}')
                print(f'The number of testing samples after rebalancing is {len(X_test)}')
                print("-" * 50)

            return X_train, X_test, y_train, y_test


class EngineeringDataLoader(DataLoader):
    """
    Class for data loading
    Parameters:
     - data_path: path to the csv file containing the data
     - target_column
     _ test_size
     - random_state
    """
    def __init__(self, data_path, target_column, test_size=0.2, imb_strat=None, random_state=42):
        super().__init__(data_path, target_column, test_size, imb_strat, random_state)
    
        self.dataframe = self.load_data()
        self.X, self.y = self.setup()
        self.X_train, self.X_test, self.y_train, self.y_test = self.train_test_split()
    
    def setup(self):
        X = self.dataframe.drop(columns=[self.target_column])
        
        # 'material' (1 is abs, 0 is pla) with numpy.where
        X['material'] = np.where(X['material'] == 'abs', 1, 0)

        # 'infill pattern' (1 is 'grid', 0 is 'honeycomb') with list comprehension
        X.infill_pattern = [1 if ip == "grid" else 0 for ip in X.infill_pattern]

        X = X.to_numpy()
        y = self.dataframe[self.target_column].to_numpy()

        assert X.shape[0] == 70
        assert X.shape[0] == y.shape[0]
        return X, y


class ChurnDataLoader(DataLoader):
    """
    Class for data loading
    """
    def __init__(self, data_path, target_column, test_size=0.2, imb_strat=None, random_state=42):
        super().__init__(data_path, target_column, test_size, imb_strat, random_state)

        self.input_preprocessing = Pipeline([
            ('categorical encoding', OrdinalEncoder())
        ])
        self.output_preprocessing = LabelEncoder()

        self.dataframe = self.load_data()
        self.X_preproc, self.y_preproc = self.split()
        self.X, self.y = self.setup()
        self.X_train, self.X_test, self.y_train, self.y_test = self.train_test_split()

    def split(self):
        # ID is arbitrary and unrelated to customer; this will try to predict utility of Cust ID (not doable)
        X = self.dataframe.drop(columns=['customerID', self.target_column]).to_numpy()  
        y = self.dataframe[self.target_column].to_numpy()

        assert X.shape[0] == 7043
        assert X.shape[0] == y.shape[0]
        return X, y

    def setup(self):
        # ID is arbitrary and unrelated to customer; this will try to predict utility of Cust ID (not doable)
        X = self.dataframe.drop(columns=['customerID', self.target_column]).to_numpy()  
        y = self.dataframe[self.target_column].to_numpy()

        # Preprocess the input features that are categorical
        # check to see that these are all the categorical columns
        categorical_features_idxs = [0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  
        X[:, categorical_features_idxs] = self.input_preprocessing.fit_transform(X[:, categorical_features_idxs])

        # Remove rows with missing values
        to_include = X[:, 18] != ' ' # Total Charges had missing values
        X = X[to_include]
        y = y[to_include]
        
        # Convert the numeric features to float
        X[:, 4] = X[:, 4].astype(float)
        X[:, 17] = X[:, 17].astype(float)
        X[:, 18] = X[:, 18].astype(float)

        # Convert the categorical features to int
        X[:, categorical_features_idxs] = X[:, categorical_features_idxs].astype(int)

        # Preprocess the output to be binary
        y = self.output_preprocessing.fit_transform(y)

        assert X.shape[0] == 7032
        assert X.shape[0] == y.shape[0]
        return X, y
