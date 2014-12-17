from character import *
from level_utils import man_dis,dis,scale_vector

class NPC(Character):
    def __init__(self,x,y,name,desc,paintLine,queue,level):
        Character.__init__(self,x,y,name,desc,paintLine,queue)
        self._goal_pos=(self._sprite.x,self._sprite.y)
        self._far_goal=None
        self._goal_Q=[]
        self._level=level
        
    #sets goal position of NPC
    def set_goal_pos(self,x,y):
        self._goal_pos=(x,y)
        
    def set_far_goal(self,x,y):
        line=self._level.raycast(self._sprite._x,self._sprite._y,x,y)
        #exists a straight shot to far goal
        if line==None:
            self.set_goal_pos(x,y)
        else:
            your_point=self._level.closest_waypoint(self._sprite._x,self._sprite._y)
            goal_point=self._level.closest_waypoint(x,y)
            
            #look up route and add it to goalQ
            self._goal_Q=self._level._navigator.pretty_path(your_point,goal_point)
            self._far_goal=(x,y)

    #moves towards a position, assuming nothing in the way using stupid methods
    def towards_old(self):
        mov=2
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

    #moves towards a position, assuming nothing in the way using lovely vectors
    def towards(self):
        mov=3
        gx,gy=self._goal_pos
        x=self._sprite.x
        y=self._sprite.y
        new_pos_vect=scale_vector(x,y,gx,gy,mov)
        deltax=int(new_pos_vect[0]-x)
        deltay=int(new_pos_vect[1]-y)

        self._sprite.x+=deltax
        self._sprite.y+=deltay
            
    def go(self):
        #if have converged on goal pos
        if dis(self._sprite._x,self._sprite._y,self._goal_pos[0],self._goal_pos[1])<2:
            #if its already following a path
            if self._goal_Q==[]:
                if self._far_goal:
                    line=self._level.raycast(self._sprite._x,self._sprite._y,self._far_goal[0],self._far_goal[1])
                    # if straight line to far goal
                    if line==None:
                        self._goal_pos=self._far_goal
                    else:
                        print "Character"+str(self._name)+" waypathing error"
                else:
                    #character has no goal in life. What a slacker!
                    pass #print "Character" +str(self._name)+" has reached goal"
            else:
                next_way=self._goal_Q.pop(0)
                self.set_goal_pos(next_way._x,next_way._y)
                self.towards()
        else:
            self.towards()

    def event(self,Q):
##        self.far_towards()
##        self.towards()
        self.go()
        Q.enqueue(10,self)
        
        
