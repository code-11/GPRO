import pyglet
from level import *
from player import *
from event_queue import *
from pyglet.window import key

class GameEngine(object):

    def __init__(self):
        self.window=pyglet.window.Window()

##        self.window.maximize()

        self.paintLine=[]

        self.lvl=Level(self.paintLine)
        self.queue=EventQueue()

        #input handler allows for polling
        self.key_handler = key.KeyStateHandler()

        #satisfies pyglet's event based fetish
        self.window.push_handlers(self.key_handler)
        self.window.push_handlers(self.on_draw)

        #access and schedule ~60fps on built in clock
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def update(self,dt):
        self.queue.dequeue_if_ready()
        
##    @window.event
    def on_draw(self):
        self.window.clear()
        for item in self.paintLine:
            item.on_draw()

def main ():
    #so beautiful, so imperitive!
    GameEngine()    
    pyglet.app.run()
    
main()
