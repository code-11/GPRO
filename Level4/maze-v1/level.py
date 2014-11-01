

from utils import *
class Level(object):


    def __init__(self):
        self.board=self.create_level()
        self.pics_ref={}
        self.permeable={0,2,3,4}
        self.climable={2,3}
        self.fallable={0,4}
        self.is_won=False
        self.characters=[]

    def create_demo (self):
        screen = []
        screen.extend([1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        screen.extend([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1])
        screen.extend([1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1])
        screen.extend([1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        screen.extend([1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1])
        screen.extend([1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        screen.extend([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1])
        screen.extend([1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1])
        screen.extend([1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1])
        screen.extend([1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1])
        screen.extend([1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1])
        screen.extend([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        screen.extend([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1])
        screen.extend([1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1])
        screen.extend([1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        return screen
# 0 empty
# 1 brick
# 2 ladder
# 3 rope
# 4 gold

    def create_level(self):
        screen = []
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0])
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1])
        screen.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,2,1,0,0,0,1,2,0,1])
        screen.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1])
        screen.extend([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0,2,0,0,0,0,3,3,3,3])
        screen.extend([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0])
        screen.extend([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1])
        screen.extend([2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,2,3,3,3,3,3,3,3,2])
        screen.extend([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2])
        screen.extend([2,0,0,0,0,0,3,3,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2])
        screen.extend([2,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,2,1,0,0,0,0,3,3,3,2,0,0,1,1,1,1,1,2])
        screen.extend([2,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,2,1,1,1,1,1,1,0,0,2,0,0,1,0,0,0,1,2])
        screen.extend([2,0,1,4,4,1,0,0,1,0,4,4,4,1,0,0,1,2,0,4,4,4,0,1,0,0,2,0,0,1,4,4,4,1,2])
        screen.extend([2,0,1,1,1,1,0,0,1,2,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,2,0,0,1,1,1,1,1,2])
        screen.extend([2,0,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,2])
        screen.extend([1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1])
        screen.extend([1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,2,0,0,0,0,0,0,0,1])
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        return screen
    
    def create_screen (self,window):
        # use this instead of Rectangle below for nicer screen
        brick = 'brick.gif'
        ladder= 'ladder.gif'
        rope= 'rope.gif'
        gold= 'gold.gif'
        pics=['buffer',brick,ladder,rope,gold]
        def image (sx,sy,what):
            return Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2),what)

        for (index,cell) in enumerate(self.board):
            if cell != 0:
                (sx,sy) = screen_pos_index(index)
                elt=image(sx,sy,pics[cell])
                self.pics_ref[index]=elt
##                elt = Rectangle(Point(sx+1,sy+1),
##                                Point(sx+CELL_SIZE-1,sy+CELL_SIZE-1))
##                elt.setFill('sienna')
                elt.draw(window)


    def create_tile(self,tile_num,index,window):
        self.board[index]=tile_num
                # use this instead of Rectangle below for nicer screen
        brick = 'brick.gif'
        ladder= 'ladder.gif'
        rope= 'rope.gif'
        gold= 'gold.gif'
        pics=['buffer',brick,ladder,rope,gold]
        
        def image (sx,sy,what):
            return Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2),what)
        
        (sx,sy) = screen_pos_index(index)
        elt=image(sx,sy,pics[tile_num])
        self.pics_ref[index]=elt
    ##                elt = Rectangle(Point(sx+1,sy+1),
    ##                                Point(sx+CELL_SIZE-1,sy+CELL_SIZE-1))
    ##                elt.setFill('sienna')
        elt.draw(window)

    def has_won(self):
        #if self.is_won==False:
        return not(4 in self.board)
        #else:
            #return True
        
#Only can be run once theoretically
    def when_won(self,player,window):
        if self.has_won() and self.is_won==False:
            self.is_won=True
            self.create_tile(2,index(34,2),window)
            self.create_tile(2,index(34,1),window)
            self.create_tile(2,index(34,0),window)
            #hack to make the player on the highest drawing level
            #I'm sure there's a function for that, but I'm lazy and it only happens once.
            player._img.undraw()
            player._img.draw(window)

    def destroy_brick(self,x,y):
        self.board[index(x,y)]=0
        self.pics_ref[index(x,y)].undraw()

    def collect_gold(self,x,y):
        self.board[index(x,y)]=0
        self.pics_ref[index(x,y)].undraw()
        #print "collecting gold in level"

    def is_permeable(self,x,y):
        try:
            return self.board[index(x,y)] in self.permeable
        except:
            return False
    def is_fallable(self,x,y):
        return self.board[index(x,y)] in self.fallable
    def is_empty(self,x,y):
        return self.board[index(x,y)] ==0
    def is_ladder(self,x,y):
        return self.board[index(x,y)] ==2
    def is_gold(self,x,y):
        return self.board[index(x,y)] ==4
    def is_brick(self,x,y):
        return self.board[index(x,y)] ==1
    def is_nonclimbable(self,x,y):
        return not(self.board[index(x,y)] in self.climable)
        
        
