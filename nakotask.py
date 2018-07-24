from celery import Task
import decorator
import pandas as pd
import nakoutils
from pyspark.sql import SparkSession

properties = nakoutils.readProperties("nakotasks.json")

def task(cls):
    
    class TaskDecorator(Task):
    	name = nakoutils.getTaskName(cls,properties)
    	sparkAppName,sparkConfigArg1,sparkConfigArg2 = nakoutils.getSparkConfigs(cls,properties) 

    	spark = SparkSession \
               .builder \
               .appName(sparkAppName) \
               .config(sparkConfigArg1, sparkConfigArg2) \
               .getOrCreate()
    	pass	
		
    return type(cls.__name__,(TaskDecorator,)+cls.__bases__,dict(cls.__dict__))
