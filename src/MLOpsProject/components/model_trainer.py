import pandas as pd
import os
from MLOpsProject import logger
from sklearn.tree import DecisionTreeClassifier
import joblib
from MLOpsProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        dtc = DecisionTreeClassifier(criterion = self.config.criterion, ccp_alpha = self.config.ccp_alpha, 
        max_depth = self.config.max_depth,random_state=self.config.random_state)
        dtc.fit(train_x, train_y)

        joblib.dump(dtc, os.path.join(self.config.root_dir, self.config.model_name))

