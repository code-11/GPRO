from utils import *
from character import *
import random
class Baddie (Character):

    BADDIE_DELAY=TIME_STEP*5
    
    def __init__ (self,x,y,window,level,player,Q):
        Character.__init__(self,'red.gif',x,y,window,level)
        self._player = player
        Q.enqueue(Baddie.BADDIE_DELAY,self)

    def sign(self,x):
        if x>0:
            return 1
        elif x<0:
            return -1
        else:
            return 0

    def can_left(self):
        return self._level.is_permeable(self._x-1,self._y)
    def can_right(self):
        return self._level.is_permeable(self._x+1,self._y)
    def can_down(self):
        return self._level.is_permeable(self._x,self._y+1)
    def get_moves(self):
        moves=[]
        if self.jump_check(0,-1):
            moves.append(MOVE['Up'])
        if self.can_left():
            moves.append(MOVE['Left'])
        if self.can_right():
            moves.append(MOVE['Right'])
        if self.can_down():
            moves.append(MOVE['Down'])
        return moves
    
    def event(self,queue):
        self.movement()
        queue.enqueue(Baddie.BADDIE_DELAY,self)

    def check_player(self):
        if self._x==self._player._x and self._y==self._player._y:
            lost(self._window)
        
    def movement(self):
        self.check_player()
        if self.should_fall():
            self.fall()
        else:
            moves=self.get_moves()
            difx=self._x-self._player._x
            dify=self._y-self._player._y
            sgnx=self.sign(-1*difx)
            sgny=self.sign(-1*dify)
            if moves!=[]:
                if (sgnx,0) in moves:
                    self.move(sgnx,0)
                elif (0,sgny) in moves:
                    self.move(0,sgny)
                    #move y direction:
                else:
                    temp=random.choice(moves)
                    self.move(temp[0],temp[1])
        
        
        
