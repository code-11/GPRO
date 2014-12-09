from drawing import *
class Block(object):
    def __init__(self,x,y,width,height,sprite):
        self._x=x
        self._y=y
        self._width=width
        self._height=height
##        print sprite
        self._sprite=sprite
    def on_draw(self):
        draw_rectangle_alt(self._x,self._y,self._width,self._height,self._sprite)
    def scale(self,factor):
        self._width=int(self._width*factor)
        self._height=int(self._height*factor)
        self._x=int(self._x*factor)
        self._y=int(self._y*factor)
        return self
    def getPos(self):
        return (self._x,self._y)
    def getX(self):
        return self._x
    def getY(self):
        return self._y
