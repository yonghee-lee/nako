from celery import Task
import decorator
import nakoutils

properties = nakoutils.readProperties("nakotasks.json")

def task(cls):
    
    taskNames = [x["taskname"] for x in properties if x["module"] == cls.__module__ and x["class"] == cls.__name__]
    
    cls.__dict__['name'] = taskNames[0]
    
    class TaskDecorator(Task):
    	pass	
		
    return type(cls.__name__,(TaskDecorator,)+cls.__bases__,dict(cls.__dict__))
