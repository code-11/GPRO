from graphics import *
LEVEL_WIDTH = 35
LEVEL_HEIGHT = 20    

CELL_SIZE = 24
WINDOW_WIDTH = CELL_SIZE*LEVEL_WIDTH
WINDOW_HEIGHT = CELL_SIZE*LEVEL_HEIGHT

TIME_STEP=.05

MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}
DIG={
    'z':(-1,1),
    'x':(1,1)
}

def screen_pos (x,y):
    return (x*CELL_SIZE+10,y*CELL_SIZE+10)

def screen_pos_index (index):
    x = index % LEVEL_WIDTH
    y = (index - x) / LEVEL_WIDTH
    return screen_pos(x,y)

def index (x,y):
    return x + (y*LEVEL_WIDTH)

def rev_index(index):
    return (index%LEVEL_WIDTH,(index/LEVEL_WIDTH))

def lost (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU LOST!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

def won (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU WON!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)
