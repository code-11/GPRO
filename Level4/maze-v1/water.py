from utils import *

#I implemented water. Water can spread in all cardinal directions but up.
#If it hasn't spread it will slow down its check frequency to spare the CPU.
#It will also spread through gold and ropes without changing the level.
#It will also slow down player movement!

class Water(object):
    WATER_DELAY_SLOW=TIME_STEP*50
    WATER_DELAY_QUICK=TIME_STEP*10

    def __init__(self,x,y,window,level,Q):
        self._x=x
        self._y=y
        self._window=window
        self._level=level
        self._queue=Q
        Q.enqueue(Water.WATER_DELAY_QUICK,self)

    def check_left(self):
        return self._level.is_empty(self._x-1,self._y)
    def check_right(self):
        return self._level.is_empty(self._x+1,self._y)
    def check_down(self):
        return self._level.is_empty(self._x,self._y+1)

    def check_down_for_permeable_not_water_or_ladder(self):
        return self.permeable_but_not_water_or_ladder(self._x,self._y+1)
    def permeable_but_not_water_or_ladder(self,x,y):
        return self._level.is_permeable(x,y) and not(self._level.is_water(x,y) or self._level.is_ladder(x,y))
            
    def spread(self):
        just_spread=False
        if self.check_down_for_permeable_not_water_or_ladder():
            if self.check_down():
                self._level.create_tile(5,index(self._x,self._y+1),self._window)
            Water(self._x,self._y+1,self._window,self._level,self._queue)
            just_spread=True
        elif not(self._level.is_permeable(self._x,self._y+1)):
            if self.check_right():
                self._level.create_tile(5,index(self._x+1,self._y),self._window)
                Water(self._x+1,self._y,self._window,self._level,self._queue)
                just_spread=True
            if self.check_left():
                self._level.create_tile(5,index(self._x-1,self._y),self._window)
                Water(self._x-1,self._y,self._window,self._level,self._queue)
                just_spread=True
        return just_spread
    def event(self,queue):
        just_spread=self.spread()
        if just_spread:
            delay=Water.WATER_DELAY_QUICK
        else:
            delay=Water.WATER_DELAY_SLOW
        
        queue.enqueue(delay,self)
