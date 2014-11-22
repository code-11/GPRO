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
import pyglet

def draw_rectangle(x1,y1,x2,y2):
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    [0, 1, 2, 0, 2, 3],
    ('v2i', (x1, y1,
             x2, y1,
             x2, y2,
             x1, y2))
    )
    
def draw_rectangle_alt(x,y,width,height):
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    [0, 1, 2, 0, 2, 3],
    ('v2i', (x, y,
             x+width, y,
             x+width, y+height,
             x, y+height))
    ),
    ('c4B', (150, 150, 255, 255))

import random
class Level (object):
    def __init__ (self,paintLine):
        self._width=50
        self._height=50
        size = self._width * self._height
        map = [0] * size
        for i in range(100):
            map[random.randrange(size)] = 1
        for i in range(50):
            map[random.randrange(size)] = 2
        self._map = map

        paintLine.append(self)

    def _pos (self,x,y):
        return x + (y*self._width);

    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]

    def on_draw(self):
        for x in xrange(self._width):
            for y in xrange(self._height):
                if self.tile(x,y)==1:
                    draw_rectangle_alt(x*10,y*10,10,10)
