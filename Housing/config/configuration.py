from housing.constants.constants import CONFIG_FILE_PATH, DATA_INGESTION_ARTIFACT_DIR, DATA_INGESTION_CONFIG_KEY, DATA_INGESTION_DATA_URL_KEY, DATA_INGESTION_INGES_DATA_DIR_KEY, DATA_INGESTION_RAWDATA_DIR_KEY, DATA_INGESTION_TEST_DIR_KEY, DATA_INGESTION_TGZ_DIR_KEY, DATA_INGESTION_TRAIN_DIR_KEY, DATA_TRANSFORMATION_ADD_BED_PER_ROOM_KEY, DATA_TRANSFORMATION_ARTIFACT_KEY, DATA_TRANSFORMATION_CONFIG_KEY, DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME, DATA_TRANSFORMATION_PREPROCESSING_DIR, DATA_TRANSFORMATION_TRANSFORMED_DIR, DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR, DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR, DATA_VALIDATION_ARTIFACT_KEY, DATA_VALIDATION_CONFIG_KEY, DATA_VALIDATION_REPORT_FILE_NAME, DATA_VALIDATION_REPORT_PAGE_FILE_NAME, DATA_VALIDATION_SCHEMA_DIR, DATA_VALIDATION_SCHEMA_FILE_NAME, MODEL_EVALUATION_ARTIFACT_KEY, MODEL_EVALUATION_CONFIG_KEY, MODEL_EVALUATION_MODEL_EVALUATION_FILE_NAME, MODEL_PUSHER_ARTIFACT_KEY, MODEL_PUSHER_CONFIG_KEY, MODEL_PUSHER_EXPORT_DIR, MODEL_TRAINER_ARTIFACT_KEY, MODEL_TRAINER_BASE_ACCURACY, MODEL_TRAINER_CONFIG_KEY, MODEL_TRAINER_MODEL_CONFIG_DIR, MODEL_TRAINER_MODEL_CONFIG_FILE_NAME, MODEL_TRAINER_MODEL_FILE_NAME, MODEL_TRAINER_TRAINED_MODEL_DIR, ROOT_DIR, TRAINING_PIPELINE_ARTIFACT_DIR_KEY, TRAINING_PIPELINE_CONFIG_KEY, TRAINING_PIPELINE_NAME_KEY
from housing.entity.config_entity import *
from housing.constants import *
from housing.util.util import *
from housing.exception import HousingException
from housing.logger import CURRENT_TIME_STAMP, logging
import sys,os
class Config:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,current_time_stamp=CURRENT_TIME_STAMP)->None:
        
        self.config_info=read_yaml(config_file_path=config_file_path)
        self.training_pipeline_config=self.get_training_pipeline_config()
        self.time_stamp=current_time_stamp


    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            artifact_dir=self.training_pipeline_config.artifact_dir
            
            data_ingestion_artifact_dir=os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)
            
            dataset_download_url=data_ingestion_info[DATA_INGESTION_DATA_URL_KEY]
            
            tgz_download_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_TGZ_DIR_KEY])
            
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_RAWDATA_DIR_KEY])
            
            ingested_dir=os.path.join(data_ingestion_artifact_dir,data_ingestion_info[DATA_INGESTION_INGES_DATA_DIR_KEY]) 
            
            ingested_test_dir=os.path.join(ingested_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])
            
            ingested_train_dir=os.path.join(ingested_dir,data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            
            data_ingestion_config=DataIngestionConfig(dataset_download_url=dataset_download_url,
            tgz_download_dir=tgz_download_dir, 
            raw_data_dir=raw_data_dir, 
            ingested_train_dir=ingested_train_dir, 
            ingested_test_dir=ingested_test_dir)
            
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config

        except Exception as e:
            
            raise HousingException(e,sys) from e
    def get_data_validation_config(self)->DataValidationConfig:
        try:
            data_validation_info=self.config_info[DATA_VALIDATION_CONFIG_KEY]
            
            artifact_dir=self.training_pipeline_config.artifact_dir

            data_validation_artifact_dir=os.path.join(artifact_dir,DATA_VALIDATION_ARTIFACT_KEY,self.time_stamp)

            schema_dir=os.path.join(ROOT_DIR,data_validation_info[DATA_VALIDATION_SCHEMA_DIR])

            schema_file_name=os.path.join(schema_dir,data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME])  
            report_file_name=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME]) 
            report_page_file_name=os.path.join(data_validation_artifact_dir,data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME])

            data_validation_config=DataValidationConfig( 
            schema_file_name=schema_file_name, 
            report_file_name=report_file_name, 
            report_page_file_name=report_page_file_name)

            logging.info(f"Data Validation config: {data_validation_config}")
            return data_validation_config

        except Exception as e:

            raise HousingException(e,sys) from e

    def get_data_tranformation_config(self)->DataTransformationConfig:
        try:
            data_tranformation_info=self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir=os.path.join(artifact_dir,DATA_TRANSFORMATION_ARTIFACT_KEY,self.time_stamp)
            add__bedroom_per_room=data_tranformation_info[DATA_TRANSFORMATION_ADD_BED_PER_ROOM_KEY]
            transformed_dir=os.path.join(data_transformation_artifact_dir,data_tranformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR])
            transformed_train_dir=os.path.join(transformed_dir,data_tranformation_info[DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR])
            tranformed_test_dir=os.path.join(transformed_dir,data_tranformation_info[DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR])
            preprocessing_dir=os.path.join(data_transformation_artifact_dir,data_tranformation_info[DATA_TRANSFORMATION_PREPROCESSING_DIR])
            preprocessed_object_file_name=os.path.join(preprocessing_dir,data_tranformation_info[DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME]) 
            data_transformation_config=DataTransformationConfig(
                add_bedroom_per_room=add__bedroom_per_room, 
                tranformed_train_dir=transformed_train_dir, 
                transformed_test_dir=tranformed_test_dir, 
                preprocessed_object_file_path=preprocessed_object_file_name
            )
            logging.info(f"Data tranformation Config:{data_transformation_config}")
            return data_transformation_config    
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_model_trainer_config(self)->ModelTrainerConfig:
        try:
            model_trainer_info=self.config_info[MODEL_TRAINER_CONFIG_KEY]
            base_accuracy=model_trainer_info[MODEL_TRAINER_BASE_ACCURACY]
            artifact_dir=self.training_pipeline_config.artifact_dir
            model_trainer_artifact_dir=os.path.join(artifact_dir,MODEL_TRAINER_ARTIFACT_KEY,self.time_stamp)
            trained_model_file_path=os.path.join(model_trainer_artifact_dir,model_trainer_info[MODEL_TRAINER_TRAINED_MODEL_DIR],model_trainer_info[MODEL_TRAINER_MODEL_FILE_NAME])
            model_configuration_file_path=os.path.join(model_trainer_artifact_dir,model_trainer_info[MODEL_TRAINER_MODEL_CONFIG_DIR],model_trainer_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME])
            model_trainer_config=ModelTrainerConfig(
                trained_model_file_path=trained_model_file_path, 
                base_accuracy=base_accuracy, 
                model_configuration_file_path=model_configuration_file_path
            )
            logging.info(f"MODEL trainer Config:{model_trainer_config}")
            return model_trainer_config 
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            model_evaluation_info=self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            artifact_dir=self.training_pipeline_config.artifact_dir
            model_evaluation_artifact_dir=os.path.join(artifact_dir,MODEL_EVALUATION_ARTIFACT_KEY,self.time_stamp)
            model_evaluation_file_path=os.path.join(model_evaluation_artifact_dir,model_evaluation_info[MODEL_EVALUATION_MODEL_EVALUATION_FILE_NAME])
            time_stamp=self.time_stamp
            model_evaluation_config=ModelEvaluationConfig(
                model_evaluation_file_path=model_evaluation_file_path, 
                time_stamp=time_stamp
                )
            logging.info(f"Model Evaluation Config:{model_evaluation_config}")
            return model_evaluation_config
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_model_pusher_config(self)->ModelPushConfig:
        try:
            model_pusher_info=self.config_info[MODEL_PUSHER_CONFIG_KEY]
            artifact_dir=self.training_pipeline_config.artifact_dir    
            model_pusher_artifact_dir=os.path.join(artifact_dir,MODEL_PUSHER_ARTIFACT_KEY,self.time_stamp)
            export_dir_path=os.path.join(model_pusher_artifact_dir,model_pusher_info[MODEL_PUSHER_EXPORT_DIR])
            model_push_config=ModelPushConfig(export_dir_path=export_dir_path)
            logging.info(f"Model Push Configuration:{model_push_config}")
            return model_push_config
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_info=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_info[TRAINING_PIPELINE_NAME_KEY],training_pipeline_info[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Configuration:{training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
            
