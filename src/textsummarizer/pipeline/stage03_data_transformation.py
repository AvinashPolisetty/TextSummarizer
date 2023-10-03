from src.textsummarizer.components.data_transformation import DataTransformation
from src.textsummarizer.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config=ConfigurationManager()
            data_tranform_config=config.get_data_tranformation_config()
            data_tranformation=DataTransformation(config=data_tranform_config)
            data_tranformation.convert()
        except Exception as e:
            raise e