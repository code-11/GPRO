from thing import *
import pyglet
import random
#
# Characters represent persons and animals and things that move
# about possibly proactively
#
class Character (Thing):
    def __init__ (self,x,y,name,desc,paintLine,queue):
        Thing.__init__(self,x,y,name,desc,paintLine,queue)
##        self._sprite = rect
        pic = pyglet.image.load('t_android_red.gif')
        self._sprite= pyglet.sprite.Sprite(pic, x=x, y=y)

    # A character has a move() method that you should implement
    # to enable movement
    def on_draw(self):
        self._sprite.draw()

    def event (self,Q):
        # WRITE ME!
        pass   

    def is_character (self):
        return True

    def is_walkable (self):
        return False
