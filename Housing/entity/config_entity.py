from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_name","report_file_name","report_page_file_name"])

DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room","tranformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainerConfig=namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy","model_configuration_file_path"])

ModelEvaluationConfig=namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPushConfig=namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineConfig=namedtuple("TrainingPipelineConfig",["artifact_dir"])