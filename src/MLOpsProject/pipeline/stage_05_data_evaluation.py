from MLOpsProject.config.configuration import ModelEvaluationConfig
from MLOpsProject.components.model_evaluation import ModelEvaluation
from MLOpsProject.config.configuration import ConfigurationManager
from MLOpsProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            logger.exception(e)
            raise e