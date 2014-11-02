from utils import *
from character import *
class Player (Character):
    def __init__ (self,x,y,window,level,Q):
        Character.__init__(self,'android.gif',x,y,window,level,Q)
        Q.enqueue(TIME_STEP,self)
        
    def event(self,queue):
        self.movement()
        queue.enqueue(self.slow_if_in_water(),self)

    def slow_if_in_water(self):
        if self._level.is_water(self._x,self._y):
            return TIME_STEP*2
        else:
            return TIME_STEP

    def die(self):
        lost(self._window)

    def movement(self):
        key = self._window.checkKey()
        if key == 'q':
            window.close()
            exit(0)
        #You can either fall or move. Not both
        if self.should_fall():
            self.fall()
        elif key in MOVE:
            (dx,dy) = MOVE[key]
            self.move(dx,dy)
            #print level.has_won()

            
        if key in DIG:
            #print "in dig "+key
            (digx,digy) =DIG[key]
            self.dig(digx,digy)

    def at_exit (self):
        return (self._y == 0)
