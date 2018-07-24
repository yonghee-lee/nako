import json

def readProperties(filepath):
    data = None

    try:
	    with open(filepath) as datafile:

	    	data = json.load(datafile)
            
    except Exception as e:
	    print(e)

    return data

def getTaskName(cls,data):
    
    taskNames = [x["taskname"] for x in data if x["module"] == cls.__module__ and x["class"] == cls.__name__]
    
    return taskNames[0]

def getSparkConfigs(cls,data):
       
    sparkAppName = [x["spark_appname"] for x in data if x["module"] == cls.__module__ and x["class"] == cls.__name__ and x["tasktype"] == "spark"]
    sparkConfigArg1 = [x["spark_config_arg1"] for x in data if x["module"] == cls.__module__ and x["class"] == cls.__name__ and x["tasktype"] == "spark"]
    sparkConfigArg2 = [x["spark_config_arg2"] for x in data if x["module"] == cls.__module__ and x["class"] == cls.__name__ and x["tasktype"] == "spark"]


    return sparkAppName[0],sparkConfigArg1[0],sparkConfigArg2[0]
