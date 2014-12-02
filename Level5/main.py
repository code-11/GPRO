import pyglet
from level import *
from player import *
from character import *
from event_queue import *
from pyglet.window import key

class GameEngine(object):

    def __init__(self):
        self.window=pyglet.window.Window(500,500)

##        self.window.maximize()

        self.paintLine=[]

        self.lvl=Level(self.paintLine)
        self.queue=EventQueue()


        #input handler allows for polling rather than push
        self.key_handler = key.KeyStateHandler()

        self.player=Player(250,250,"Player",self.paintLine,self.queue,self.key_handler,self.lvl)
##        self.player.materialize(500,500)
        
        Character(100,100,"Trusty","Chester",self.paintLine,self.queue)    

        #satisfies pyglet's event based fetish
        self.window.push_handlers(self.key_handler)
        self.window.push_handlers(self.on_draw)

        #access and schedule ~30fps on built in clock
        pyglet.clock.schedule_interval(self.update, 1/120.0)#1/120.0)

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