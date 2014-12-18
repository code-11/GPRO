from npc import *
class Rand_NPC(NPC):
    def __init__(self,x,y,name,desc,image_name,paintLine,queue,level):
        NPC.__init__(self,x,y,name,desc,image_name,paintLine,queue,level)
        
    def wander_ai(self):
        if self._far_goal==None:
            point=self._level._navigator.random_waypoint()
            self.set_far_goal(point._x,point._y)
            
    def event(self,Q):
        self.wander_ai()
        self.go()
        Q.enqueue(10,self)
