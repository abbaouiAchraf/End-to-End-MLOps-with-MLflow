from MLOpsProject import logger
from MLOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLOpsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} <<<<")
    DataIngestion = DataIngestionTrainingPipeline()
    DataIngestion.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<< \n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} <<<<")
    DataValidation = DataValidationTrainingPipeline()
    DataValidation.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<< \n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> Starting {STAGE_NAME} <<<<")
    DataTransformation = DataTransformationTrainingPipeline()
    DataTransformation.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<< \n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e