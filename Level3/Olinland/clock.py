import Queue
class Clock (object):

    def __init__ (self,time):
        self.todo=Queue.PriorityQueue()
        self.time=time
        #self.name_to_function={}
    def register(self,f,priority):
        self.todo.put((priority,f))
        #self.name_to_function["fname"]=f
    def unregister():
        pass
    def tick(self):
        temp_queue=Queue.PriorityQueue()
        while not(self.todo.empty()):
            tup=self.todo.get()
            to_run=tup[1]
            priority=tup[0]
            #put the method back so it can be called in previous rounds
            temp_queue.put(tup)
            to_run(self.time)
        self.todo=temp_queue
        self.time+=1
        
            
        
    # FIX ME
