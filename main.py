from src.textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainigPipeline
from src.textsummarizer.pipeline.stage02_data_validation import DataValidationTrainigPipeline
from src.textsummarizer.pipeline.stage03_data_transformation import DataTransformationPipeline
from src.textsummarizer.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from src.textsummarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
from src.textsummarizer.logging import logging
from exception import CustomException
import sys

Stage_name="Data Ingestion Stage"

try:
    logging.info(f">>>> {Stage_name} started <<<<<")
    data_ingestion=DataIngestionTrainigPipeline()
    data_ingestion.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)


Stage_name="Data Validation Stage"

try:
    logging.info(f">>>> {Stage_name} started <<<<<")
    data_validation=DataValidationTrainigPipeline()
    data_validation.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)


Stage_name="Data Transformation Stage"

try:
    logging.info(f">>>> {Stage_name} started <<<<<")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)


Stage_name="Model Trainer Stage"

try:
    logging.info(f">>>> {Stage_name} started <<<<<")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)


Stage_name="Model Evaluation Stage"

try:
    logging.info(f">>>> {Stage_name} started <<<<<")
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logging.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)




