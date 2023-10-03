from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_validation import DataValidation
from exception import CustomException
import sys

class DataValidationTrainigPipeline:
        def __init__(self):
            pass

        def main(self):
            try:

                config=ConfigurationManager()
                data_validation_config=config.get_data_validation_config()
                data_validation=DataValidation(config=data_validation_config)
                data_validation.validate_all_files_exists()
            except Exception as e:
                raise e