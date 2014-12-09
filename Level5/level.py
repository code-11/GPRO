#############################################################
# 
# The description of the world and the screen which displays
# the world
#
# A level contains the background stuff that you can't really
# interact with. The tiles are decorative, and do not come
# with a corresponding object in the world. (Though you can
# change that if you want.)
#
# Right now, a level is described using the following encoding
#
# 0 empty   (light green rectangle)
# 1 grass   (green rectangle)
# 2 tree    (sienna rectangle)
#
# you'll probably want to make nicer sprites at some point.


#
# This implements a random level right now. 
# You'll probably want to replace this with something that 
# implements a specific map -- perhaps of Olin?
#



from block import *
from waypoint import *
from navigator import *
import random
class Level (object):
    def scale(self,factor):
        for block in self._map:
            block.scale(factor)
        self._navigator.scale(factor)
    def level_one(self,paintLine):
        col=(.1,.5,.25)
        
        _map=[]
        _map.append(Block(100,0,750,30,col))      #A
        _map.append(Block(700,0,600,30,col))      #B
        _map.append(Block(450,0,30,200,col))      #C
        _map.append(Block(950,0,30,170,col))      #D
        _map.append(Block(1300,0,30,300,col))     #E 1200
        _map.append(Block(1300,400,30,200,col))   #E2
        _map.append(Block(1300,700,30,200,col))   #E3
        _map.append(Block(1300,1000,30,200,col))  #E4
        _map.append(Block(100,1200,1230,30,col))  #F
        _map.append(Block(1200,400,100,30,col))   #0
        _map.append(Block(950,400,100,30,col))    #N
        _map.append(Block(950,300,30,300,col))    #M
        _map.append(Block(950,700,30,300,col))    #P
        _map.append(Block(950,1100,30,120,col))   #R
        _map.append(Block(870,900,100,30,col))    #Q
        _map.append(Block(-150,900,770,30,col))   #H
        _map.append(Block(450,1100,30,120,col))   #S
        _map.append(Block(1300,1000,200,30,col))  #U
        _map.append(Block(1500,300,30,730,col))   #V
        _map.append(Block(1300,300,200,30,col))   #W
        _map.append(Block(450,700,30,300,col))    #T
        _map.append(Block(450,300,30,300,col))    #L
        _map.append(Block(-150,400,600,30,col))   #J
        _map.append(Block(100,800,30,400,col))    #G
        _map.append(Block(-150,400,30,500,col))   #I
        _map.append(Block(100,0,30,700,col))      #K

        brown=(.5,.3,.1)
        _map.append(Block(670,400,170,350,brown)) #stairs
        _map.append(Block(590,1000,250,110,brown)) #dining table
        _map.append(Block(1200,1100,30,30,brown)) #hall table
        _map.append(Block(1200,800,30,30,brown)) #hall table
        _map.append(Block(1200,150,30,30,brown)) #sitting room table
        _map.append(Block(200,500,150,60,brown)) #kitchenette table
        self._map=_map

        waypoints=[]
        a=Waypoint(300,250)
        b=Waypoint(550,250)
        c=Waypoint(900,250)
        d=Waypoint(1100,250)
        e=Waypoint(1100,350)
        f=Waypoint(1300,350)
        g=Waypoint(1100,100)
        
        a.conn(b)

        b.conn(a)
        b.conn(b)
        b.conn(c)

        c.conn(b)
        c.conn(d)

        d.conn(c)
        d.conn(e)
        d.conn(f)
        d.conn(g)

        e.conn(d)
        e.conn(f)

        f.conn(e)
        f.conn(d)

        g.conn(d)

        
        

        

        waypoints+=[a,b,c,d,e,f,g]

        self._navigator=Navigator(waypoints)
        
        
    def __init__ (self,paintLine):
        self._width=50
        self._height=50
        size = self._width * self._height
        
        
        self.level_one(paintLine)
        self.scale(.25)

        paintLine.append(self)

    def _pos (self,x,y):
        return x + (y*self._width);
    
##    def inv_pos(self,index):
##        return (index%self._width,index/self._width)
    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]

    # Does a point with graphics coordinates x and y collide with the level?
    def collide(self,graph_x,graph_y):
        for block in self._map:
            if self.withinBox(graph_x,graph_y,block):
                return True
        return False
    
    def withinBox(self,x,y,block):
        return (x>block._x and x<block._x+block._width) and (y>block._y and y<block._y+block._height)

    def on_draw(self):
        for block in self._map:
                block.on_draw()
        self._navigator.on_draw()
