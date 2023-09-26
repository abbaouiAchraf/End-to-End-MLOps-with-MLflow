import os
from MLOpsProject import logger
from MLOpsProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_column(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir, sep=';')
            all_cols = list(data.columns)
            all_schema = self.config.all_schema
            # print(all_schema)

            for col in all_cols:
                if col not in all_schema.keys(): 
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        break
                else:
                    if data[col].dtype == all_schema[col]:
                        validation_status = True
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else: 
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                            break
        except Exception as e:
            logger.error(e)
            raise e