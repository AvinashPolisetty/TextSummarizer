from src.textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainigPipeline
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


