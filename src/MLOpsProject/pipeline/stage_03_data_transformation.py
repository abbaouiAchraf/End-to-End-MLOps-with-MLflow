from MLOpsProject.config.configuration import DataTransformationConfig
from MLOpsProject.components.data_transformation import DataTransformation
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open("artifacts/data_validation/status.txt") as f:
                status = f.read().split(" ")[-1]
            if status == "True":    
                config_manager = ConfigurationManager()
                data_transformation_config = config_manager.get_data_transformation_config()

                # Initialize data transformation
                data_transformation = DataTransformation(data_transformation_config)

                # Apply data transformations
                data_transformation.handle_duplicates()
                data_transformation.handle_missing_values()
                data_transformation.encoding()
                data_transformation.feature_scaling()
                # data_transformation.handle_imbalanced_data()
                data_transformation.train_test_split()
            else:
                raise Exception("Data Schema is not valid")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} <<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> Completed {STAGE_NAME} <<<< \n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e