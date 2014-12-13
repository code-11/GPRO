from character import *

class NPC(Character):
    def __init__(self,x,y,name,desc,paintLine,queue,level):
        Character.__init__(self,x,y,name,desc,paintLine,queue)
        self._goal_pos=(self._sprite.x,self._sprite.y)
        self._level=level
        
    #sets goal position of NPC
    def set_goal_pos(self,x,y):
        self._goal_pos=(400,400)

    #moves towards a position, assuming nothing in the way
    def towards(self):
        mov=2
        goal_size=3
        gx,gy=self._goal_pos
        x=self._sprite.x
        y=self._sprite.y
        if x>gx:
            self._sprite.x-=mov
        elif x<gx:
            self._sprite.x+=mov

        if y>gy:
            self._sprite.y-=mov
        elif y<gy:
            self._sprite.y+=mov


    def event(self,Q):
        self.towards()
        Q.enqueue(10,self)
        
        
