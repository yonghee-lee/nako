from __future__ import absolute_import, unicode_literals
from celery import current_app
from celery.bin import worker
 
def import_task(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def read_tasks():
	pass

class TaskLoader:

	def __init__(self):
		self.task = import_task('mytest.MyTest')

if __name__=='__main__':
	app = current_app._get_current_object()
	worker = worker.worker(app=app)
	options = {
		'loglevel': 'INFO',
	}
	
	app.tasks.register(TaskLoader().task)
	worker.run(**options)

