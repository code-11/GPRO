from block import *
from drawing import *
class Waypoint(Block):
    def __init__(self,x,y,name):
        Block.__init__(self,x,y,10,10,"")
        self._points=[]
        self._name=name
    def on_draw(self):
        draw_rectangle_alt(self._x,self._y,self._width,self._height,(1,1,1))
        for p in self._points:
            draw_line(self._x,self._y,p.getX(),p.getY(),(1,0,0))
    def conn(self,point):
        self._points.append(point)
    def __repr__(self):
        return self._name
