from npc import *
class Target_NPC(NPC):
    def __init__(self,x,y,name,desc,image_name,paintLine,queue,level,target):
        NPC.__init__(self,x,y,name,desc,image_name,paintLine,queue,level)
        self._target=target
        self._count=0
        
    def target_ai(self):
        self.set_far_goal(self._target._sprite.x,self._target._sprite.y)
##        if self._far_goal==None:
##            point=self._level._navigator.random_waypoint()
##            self.set_far_goal(point._x,point._y)
            
    def event(self,Q):
        self._count+=1
        if self._count==3:
            self.target_ai()
            self._count=0
        self.go()
        Q.enqueue(10,self)
