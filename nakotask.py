from celery import Task
import decorator

def task(cls):
    class Decorator(Task):
    	pass
    return type(cls.__name__,(Decorator,)+cls.__bases__,dict(cls.__dict__))
