import pyglet
from character import *
from global_vars import SPRITE_SIZE,PLAYER_ACTION_RATE
from pyglet.window import key
from pyglet.gl import glTranslatef

#
# The Player character
#
class Player (Character):
    def __init__ (self,x,y,name,paintLine,queue,key_handler,lvl):
        Character.__init__(self,x,y,name,"Yours truly",'t_android_red.gif',paintLine,queue)
##        log("Player.__init__ for "+str(self))
##        pic = 't_android_red.gif'
##        pic = pyglet.image.load('t_android_red.gif')
##        pic = pyglet.image.load('castro.gif')
##        self._sprite= pyglet.sprite.Sprite(pic, x=x, y=y)
        self.key_handler=key_handler
        queue.enqueue(PLAYER_ACTION_RATE,self)
        self.lvl=lvl
##        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),pic)
        
    def is_player (self):
        return True

    def on_draw(self):
        self._sprite.draw()

    def allowed(x,y):
        pass

    #returns True if one of the corners of the sprite interacts with the environment
    #There is a 1px buffer around the sprite enforced by all the crazy -1 and +1
    def check_all_corners(self,xoff=0,yoff=0):
        lowl=self.lvl.collide(self._sprite.x+xoff,self._sprite.y-1+yoff)
        lowr=self.lvl.collide(self._sprite.x+SPRITE_SIZE-1+xoff,self._sprite.y-1+yoff)
        highl=self.lvl.collide(self._sprite.x+xoff,self._sprite.y+SPRITE_SIZE-1+yoff)
        highr=self.lvl.collide(self._sprite.x+SPRITE_SIZE-1+xoff,self._sprite.y+SPRITE_SIZE-1+yoff)
        return (lowl or lowr or highl or highr)

    def event(self,Q):
##        print self.check_all_corners(0,3)
        if self.key_handler[key.ENTER]:
            print "x,y :"+str(self._sprite.x)+","+str(self._sprite.y)
        
        mov=3
        if self.key_handler[key.UP] and not(self.check_all_corners(0,mov)):
            glTranslatef(0,-mov,0)
            self._sprite.y+=mov
##            self.lvl.addY-=mov
        elif self.key_handler[key.RIGHT]and not(self.check_all_corners(mov,0)):
            glTranslatef(-mov,0,0)
            self._sprite.x+=mov
##            self.lvl.addX-=mov
        elif self.key_handler[key.DOWN]and not(self.check_all_corners(0,-mov)):
            glTranslatef(0,mov,0)
            self._sprite.y-=mov
##            self.lvl.addY+=mov
        elif self.key_handler[key.LEFT]and not(self.check_all_corners(-mov,0)):
            glTranslatef(mov,0,0)
            self._sprite.x-=mov

##            self.lvl.addX+=mov

        Q.enqueue(PLAYER_ACTION_RATE,self)
    # The move() method of the Player is called when you 
    # press movement keys. 
    # It is different enough from movement by the other
    # characters that you'll probably need to overwrite it.
    # In particular, when the Player move, the screen scrolls,
    # something that does not happen for other characters

    def move (self,dx,dy):
        # WRITE ME!
        pass
