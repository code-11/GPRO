# in case you don't know, this line lets you use
# glViewport instead of pyglet.gl.glViewport, etc.

from pyglet.gl import *

# some people think you shouldn't import
# the entire gl namespace, but it makes it
# easier when you're learning OpenGL and
# pyglet at the same time...

def on_resize(width, height):

    # set up the windowing transform so
    # it draws to the entire window

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # to center the camera, you want
    # the left edge to be at -width/2
    # and the right edge at width/2

    w = window._width/2
    h = window._height/2

    # now, glOrtho specifies the size of the
    # 'viewport' in the sense you were thinking,
    # i.e. the 'size' covered by the camera

    glOrtho(-w, w, -h, h, -1.0, 1.0)

    # now, the camera is centered in the window
    # and we can move it around when we draw
    # the scene...

def on_draw():

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # position the camera, per Drew's advice...
    # the 'size' will be whatever you set with
    # glOrtho in the resize handler...

    glTranslatef(-camera.pos.x,
                 -camera.pos.y,
                 -camera.pos.z)

    # now draw your scene

    for surface in scene:

        # (push and pop let you save
        #  the camera position between
        #  drawing each object)

        glPushMatrix()
        glTranslatef(surface.pos.x,
                     surface.pos.y,
                     surface.pos.z)
        surface.draw()
        glPopMatrix()
