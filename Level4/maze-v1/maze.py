#
# MAZE
# 
# Example game
#
# Version without baddies running around
#
from utils import *
from character import *
from player import *
from baddie import *
from level import *
from event_queue import *
import time



def main ():

    window = GraphWin("Maze", WINDOW_WIDTH+20, WINDOW_HEIGHT+20)

    rect = Rectangle(Point(5,5),Point(WINDOW_WIDTH+15,WINDOW_HEIGHT+15))
    rect.setFill('sienna')
    rect.setOutline('sienna')
    rect.draw(window)
    rect = Rectangle(Point(10,10),Point(WINDOW_WIDTH+10,WINDOW_HEIGHT+10))
    rect.setFill('white')
    rect.setOutline('white')
    rect.draw(window)

    level = Level(window)

    Q=Event_Queue()
    
    level.pics_ref={}
    level.board=level.create_second_level()

    screen = level.create_screen(window)
    
    p = Player(17,18,window,level,Q)

    baddie1 = Baddie(19,2,window,level,p,Q)
    baddie2 = Baddie(19,7,window,level,p,Q)
    baddie3 = Baddie(24,18,window,level,p,Q)

    level.characters.extend([p,baddie1,baddie2,baddie3])

    #screen = level.create_screen(window)
    level.handle_water(window,Q)

    #adding the level to the queue refreshes moving characters
    #every once and awhile. Its a workaround for a graphical glitch
    #that since the water is drawn second you appear behind the water.
    Q.enqueue(TIME_STEP*120,level)
    
    while not p.at_exit():
        Q.dequeue_if_ready()
        if level.has_won():
            level.when_won(p,window)
        time.sleep(TIME_STEP)

    won(window)

if __name__ == '__main__':
    main()
