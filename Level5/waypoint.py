from block import *
from drawing import *
class Waypoint(Block):
    def __init__(self,x,y,paintLine):
        Block.__init__(self,x,y,10,10,"NA")
        paintLine.append(self)
    def on_draw(self):
        draw_rectangle_alt(self._x,self._y,self._width,self._height,(1,1,1))
