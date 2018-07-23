import json

def readProperties(filepath):
    data = None

    try:
	    with open(filepath) as datafile:

	    	data = json.load(datafile)
            
    except Exception as e:
	    print(e)

    return data

def getTaskName(filepath,cls_module,cls_name):
    taskName = None
    data = readProperties(filepath)
    taskName = [x["taskname"] for x in data if x["module"] == cls_module and x["class"] == cls_name]
    print(len(taskName))
    return taskName[0]
