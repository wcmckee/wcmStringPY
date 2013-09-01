from retask import Task
from retask import Queue

queue = Queue('examples')

info1 = {'user':'wcmckee', 'url':'http://wcmckee.com'}
info2 = {'user':'lmckee', 'url':'https://github.com/drhealsgood'}
task1 = Task(info1)
task2 = Task(info2)
queue.connect()
queue.enqueue(task1)
queue.enqueue(task2)


