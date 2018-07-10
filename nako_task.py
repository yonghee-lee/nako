from abc import abstractmethod
from spark_celery import SparkCeleryApp, SparkCeleryTask, cache, main

class NakoTask(SparkCeleryTask):
	
	BROKER_URL = 'redis://localhost:6379/0'
	CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
	
	def __init__(self,taskName='ananymous'):
		app = SparkCeleryApp(broker=BROKER_URL, backend=CELERY_RESULT_BACKEND, sparkconf_builder=sparkconfig_builder(taskName))

	def sparkconfig_builder(self):
    	from pyspark import SparkConf
    	return SparkConf().setAppName('SparkCeleryTask') \
        	.set('spark.dynamicAllocation.enabled', 'true') \
        	.set('spark.dynamicAllocation.schedulerBacklogTimeout', 1) \
        	.set('spark.dynamicAllocation.minExecutors', 1) \
        	.set('spark.dynamicAllocation.executorIdleTimeout', 20) \
        	.set('spark.dynamicAllocation.cachedExecutorIdleTimeout', 60)

	@abstractmethod
	def get_data(self): raise NotImplementedError
	@abstractmethod
	def run(self): raise NotImplementedError



