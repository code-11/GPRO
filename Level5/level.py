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
    
def draw_rectangle_alt(x,y,width,height,color=(0,0,0)):
    pyglet.graphics.glColor3f(color[0],color[1],color[2])
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    [0, 1, 2, 0, 2, 3],
    ('v2i', (x, y,
             x+width, y,
             x+width, y+height,
             x, y+height))
    )

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

    # Does a point with graphics coordinates x and y collide with the level?
    def collide(self,graph_x,graph_y):
        for x in xrange(self._width):
            for y in xrange(self._height):
                if self._map[self._pos(x,y)]==1:
                    graph_x_blk=self.transX(x)
                    graph_y_blk=self.transY(y)
                    collision=self.withinBox(graph_x,graph_y,graph_x_blk,graph_y_blk)
                    if collision:
                        return collision
        return False
    #Transform grid corrds to graphical coords.
    def transX(self,x):
        return x*10

    def transY(self,y):
        return y*10
    
    def withinBox(self,x,y,x2,y2):
        return (x>x2 and x<x2+20) and (y>y2 and y<y2+20)

    def on_draw(self):
        for x in xrange(self._width):
            for y in xrange(self._height):
                if self.tile(x,y)==1:
                    #print self.addX
                    draw_rectangle_alt(x*10,y*10,20,20,(0,.5,.25))
                    #print x
