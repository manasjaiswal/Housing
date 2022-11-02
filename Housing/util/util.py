import yaml
from housing.exception import HousingException

def read_yaml(config_file_path):
    config_info=None
    try:
        with open(config_file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e