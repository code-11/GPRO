import pyglet
from level import *
from player import *
from npc import *
from rand_npc import *
from event_queue import *
from target_npc import *
from global_vars import *
from pyglet.window import key

class GameEngine(object):

    def __init__(self):
        self.window=pyglet.window.Window(WINDOW_X,WINDOW_Y)

##        self.window.maximize()

        self.paintLine=[]

        self.lvl=Level(self.paintLine)
        self.queue=EventQueue()


        #input handler allows for polling rather than push
        self.key_handler = key.KeyStateHandler()

        self.player=Player(250,250,"Player",self.paintLine,self.queue,self.key_handler,self.lvl)
##        self.player.materialize(500,500)
        
##        test=Rand_NPC(170,370,"","",self.paintLine,self.queue,self.lvl)
        #test.set_far_goal(1260,1160)
        #test.set_far_goal(0,450)
        #test.set_far_goal(170,450)

        Rand_NPC(1000,370,"","","castro.gif",self.paintLine,self.queue,self.lvl)
        Rand_NPC(706,1000,"","","kennedy.gif",self.paintLine,self.queue,self.lvl)
##        Target_NPC(-11,750,"","","khrushchev.gif",self.paintLine,self.queue,self.lvl,self.player)
        
##        Rand_NPC(170,1000,"","",self.paintLine,self.queue,self.lvl)
##        Rand_NPC(800,500,"","",self.paintLine,self.queue,self.lvl)

        
        #satisfies pyglet's event based fetish
        self.window.push_handlers(self.key_handler)
        self.window.push_handlers(self.on_draw)

        #access and schedule ~60fps on built in clock
        pyglet.clock.schedule_interval(self.update, FRAME)#1/120.0)

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
