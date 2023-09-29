import os
from MLOpsProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from MLOpsProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path, sep=";")
    
    def categorical_columns(self):
        categorical_columns = []
        for col in self.data.columns:
            if self.data[col].dtype == "object":
                categorical_columns.append(col)
        return categorical_columns

    def handle_missing_values(self):
        imputer = SimpleImputer(strategy='most_frequent')
        self.data[self.categorical_columns()] = imputer.fit_transform(self.data[self.categorical_columns()])
        self.data.fillna(self.data.mean(), inplace=True)
    def handle_imbalanced_data(self):
        target = self.config.schema.TARGET_COLUMN.name
        X = self.data.drop(target, axis=1)
        y = self.data[target]

        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X, y)

        # Create a new DataFrame with the resampled data
        resampled_df = pd.concat([
            pd.DataFrame(X_resampled, columns=X.columns),
            pd.DataFrame(y_resampled, columns=[target])
        ], axis=1)

        self.data = resampled_df

    def handle_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def handling_outliers(self):
        pass  # TODO: Add outlier handling code later

    def binning(self):
        categorical_columns = self.categorical_columns()
        for i in categorical_columns:
            self.data[i] = pd.cut(self.data[i], bins=5, labels=False)

    def encoding(self):
        categorical_columns = self.categorical_columns()
        label = LabelEncoder()
        for i in categorical_columns:
            self.data[i] = label.fit_transform(self.data[i])

    def feature_scaling(self):
        scaler = StandardScaler()
        scalled_columns = self.data.columns.drop(self.config.schema.TARGET_COLUMN.name)
        self.data[scalled_columns] = scaler.fit_transform(self.data[scalled_columns])

    def train_test_split(self):
        train, test = train_test_split(self.data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info("Splitted data into train and test set")
        logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")