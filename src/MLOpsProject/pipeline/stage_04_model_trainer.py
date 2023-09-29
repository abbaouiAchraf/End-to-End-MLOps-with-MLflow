from MLOpsProject.config.configuration import ModelTrainerConfig
from MLOpsProject.components.model_trainer import ModelTrainer
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            logger.exception(e)
            raise e