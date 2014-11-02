from utils import *
from hole import *
class Character (object):
    def __init__ (self,pic,x,y,window,level,Q):
        (sx,sy) = screen_pos(x,y)
        self._img = Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2+2),pic)
        self._window = window
        self._img.draw(window)
        self._x = x
        self._y = y
        self._level = level
        self._score =0
        self._queue=Q
        self._dead=False

    def same_loc (self,x,y):
        return (self._x == x and self._y == y)

    #No jumping allowed...yet
    #Returns true if not a jump
    def jump_check(self,dx,dy):
        return not(dy==-1 and self._level.is_nonclimbable(self._x,self._y))

    #If what you're on is empty or gold, and what is below isn't ladder but is permeable, fall
    def should_fall(self):
        return self._level.is_fallable(self._x,self._y)and self._level.is_permeable(self._x,self._y+1) and not(self._level.is_ladder(self._x,self._y+1)) 

    def fall(self):
        self._y = self._y+1
        self._img.move(0,1*CELL_SIZE)

    def collect_gold(self):
        if self._level.is_gold(self._x,self._y):
            #print "collecting gold in character"
            self._level.collect_gold(self._x,self._y)
            self._score+=1

    def dig(self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if self._level.is_brick(tx,ty) and self._level.is_empty(tx,self._y)and not(self.should_fall()):
            self._level.destroy_brick(tx,ty)
            Hole(tx,ty,self._window,self._level,self._queue)

    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        #print self.should_fall()
        self.collect_gold()
        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            #if self.should_fall():
                #ty= self._y-dy+1
                #self.fall()
            if self._level.is_permeable(tx,ty) and self.jump_check(dx,dy):
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)
                
        
