import Queue
class Clock (object):

    def __init__ (self,time):
        self.todo=Queue.PriorityQueue()
    def register(f,priority):
        self.todo.put((priority,f))
    def unregister():
        pass
    # FIX ME
