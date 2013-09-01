from retask import Task
from retask import Queue
import time
import pprint
queue = Queue('example')
queue.connect()
task = queue.wait()
pprint.pprint(task.data)
time.sleep(15)
queue.send(task, "We received your information dear %s" % task.data['user'])

