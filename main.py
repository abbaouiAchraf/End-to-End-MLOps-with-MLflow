from MLOpsProject import logger
from MLOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} <<<<")
    DataIngestion = DataIngestionTrainingPipeline()
    DataIngestion.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<< \n\nx=====================x")
except Exception as e:
    logger.exception(e)
    raise e
