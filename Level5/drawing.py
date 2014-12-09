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
def draw_line(x1,y1,x2,y2,color=(0,0,0)):
    pyglet.graphics.glColor3f(color[0],color[1],color[2])
    pyglet.graphics.draw(2,pyglet.gl.GL_LINES,
    ('v2i', (x1, y1, x2, y2))
    )
