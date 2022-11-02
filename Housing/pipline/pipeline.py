from collections import namedtuple
from datetime import datetime
import uuid
from housing.config.configuration import Config
from housing.logger import logging
from housing.exception import HousingException
from threading import Thread
from typing import List

from multiprocessing import Process
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.component.data_ingestion import DataIngestion
import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd


class Pipeline():

    def __init__(self, config:Config=Config()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e

    def run_pipeline(self):
        self.start_data_ingestion()
