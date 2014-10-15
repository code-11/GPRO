from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc):
        MobileThing.__init__(self,name,loc)
        self._done=False
        
    def done(self):
        return self._done

    def complete(self):
        self._done=True
        self._name="done-"+self._name
        self._description+=".This homework is done!"
    
    def is_homework (self):
        return True
