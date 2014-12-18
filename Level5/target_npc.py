from npc import *
from drawing import draw_line
from global_vars import DEBUG
class Target_NPC(NPC):
    def __init__(self,x,y,name,desc,image_name,paintLine,queue,level,target):
        NPC.__init__(self,x,y,name,desc,image_name,paintLine,queue,level)
        self._target=target
        self._count=0
        
    def target_ai(self):
        self.set_far_goal(self._target._sprite.x,self._target._sprite.y)
            
    def event(self,Q):
        self._count+=1
        # AI spazzes out if I make this 2.
        # Not really sure why, but I'm not complaining
        if self._count==3:
            self.target_ai()
            self._count=0
        self.go()
        Q.enqueue(10,self)
    def on_draw(self):
        self._sprite.draw()
        if DEBUG:
            draw_line(self._sprite.x,self._sprite.y,self._target._sprite.x,self._target._sprite.y,(0,0,1))
