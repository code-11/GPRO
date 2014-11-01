from utils import *
class Hole(object):
    HOLE_DELAY=TIME_STEP*20
    
    def __init__(self,x,y,window,level,Q):
        self._x=x
        self._y=y
        self._window=window
        self._level=level
        Q.enqueue(Hole.HOLE_DELAY,self)

    def close(self):
        for moving_thing in self._level.characters:
            if moving_thing._x==self._x and moving_thing._y==self._y:
                moving_thing.die()
                #print "crunch"
        self._level.create_tile(1,index(self._x,self._y),self._window)

    def event(self,queue):
        self.close()
