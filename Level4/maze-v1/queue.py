import Queue
class Event_Queue(object):
    def __init__(self):
        self.Q=Queue.PriorityQueue()
        
    def __str__(self):
        newQ=Queue.PriorityQueue()
        to_print=[]
        while not(self.Q.empty()):
            when,obj=self.Q.get()
            to_print.append((when,obj))
            newQ.put((when,obj))
        self.Q=newQ
        return str(to_print)
    
    def enqueue(self,when,obj):
        self.Q.put((when,obj))
        
    def decrease(self):
        newQ=Queue.PriorityQueue()
        while not(self.Q.empty()):
            when,obj=self.Q.get()
            newQ.put((when-TIME_STEP,obj))
        self.Q=newQ
        
    def dequeue_if_ready(self):
        self.decrease()
        while not(self.Q.empty()):
            when,obj=self.Q.get()
            if when<=0:
                print str(when)+"<=0"
                print "running event on "+ str(obj)
            else:
                self.Q.put((when,obj))
                break

queue=Event_Queue()
queue.enqueue(1,"a")
queue.enqueue(0,"c")
queue.enqueue(4,"j")
queue.enqueue(-3,"g")
queue.enqueue(100,"o")
queue.dequeue_if_ready()
