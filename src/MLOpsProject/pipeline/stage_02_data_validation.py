from MLOpsProject.config.configuration import DataValidationConfig
from MLOpsProject.components.data_validation import DataValidation
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_column()

if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} <<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> Completed {STAGE_NAME} <<<<\n\nx=====================x")
    except Exception as e:
        logger.exception(e)
        raise e