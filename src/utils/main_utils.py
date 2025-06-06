import sys
from typing import Dict,Tuple
import os
import pandas as pd
import pickle
import yaml
import boto3

from src.constant import *
from src.exception import CustomException
from src.logging import logging


class MainUtils:
    def __init__(self) -> dict:
        pass

    def read_yaml_file(self, filename :str) -> dict:
        try:
          with open(filename,"rb") as yaml_file:
             return yaml.safe_load(yaml_file)
          
        except Exception as e:
           raise CustomException(e,sys) from e  
        
    def read_schema_config_filre(self) -> dict:
       try:
          schema_config = self.read_yaml_file(os.path.join("config","schema.yaml"))  
          return schema_config
       
       except Exception as e:
          raise CustomException(e,sys) from e
       
    @staticmethod
    def load_object(file_path):
       try:
          with open(file_path,"rb") as file_obj:
             return pickle.load(file_obj) 

       except Exception as e :
           
           logging.info('Exception occured in load_object function utils')
           raise CustomException(e,sys)
       


          

