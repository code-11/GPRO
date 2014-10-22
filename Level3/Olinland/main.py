
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *
from trollhunter import *
from badninja import *
from butterfly import *
from needy import *
from hermit import *

REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    mh353 = Room('Riccardo Office')
    mh3rd = Room('Milas Hall Third Floor')
    mh2nd = Room('Milas Hall Second Floor')
    mh1st = Room('Milas Hall First Floor')
    oval = Room('Oval',"The Oval, smack in the center of Olin College.")
    ac1st = Room('Academic Center First Floor')
    ac113 = Room('Academic Center 113')
    cc1st = Room('Campus Center First Floor')
    westh = Room('West Hall')
    easth = Room('East Hall')
    babson = Room('Babson College')

    test =Room('The Void')
    biconnect(oval, 'up',test)

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    #biconnect(mh1st, 'north',  oval)
    #biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  westh)
    biconnect(westh, 'east',  easth)
    #biconnect(oval, 'north',  babson)
    #biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)

    # The player is the first 'thing' that has to be created

    Player('Blubbering-Fool', oval)

    Radar('handy radar',oval,"Its an N-dimensional object locator. Hard to look at it for long periods.") 
    Thing('blackboard', ac113,"Dustier than a white board")
    #Thing('lovely-trees', oval,"There are no trees; they are not real")
    MobileThing('cs-book', oval,"Looks thick, I wonder if there's a cheap PDF version")
    MobileThing('math-book', oval,"It doesn't have the answers in the back. It is useless to me.")

##    temp_npc=NPC('ebenezer',oval,5,1)
##    Player.clock.register(temp_npc.move_and_take_stuff,8)

    #temp_th=TrollHunter("Jack 'o Blades",oval,1)
    #Player.clock.register(temp_th.search_and_destroy,9)
    
    Computer('hal-9000', mh2nd)
    Computer('johnny-5', easth)

    temp_prof=Professor('Riccardo',mh353,random.randint(1,5),2)
    Player.clock.register(temp_prof.lecture,8)

    #Needy('Archibald',oval,'done-hw-7','Mild mannered explorer')

    Hermit('Plato',oval,'This grumpy man wears nothing but a toga...ick')

##    flutterby=ButterFly('Cloudless Sulphur',oval)
##    Player.clock.register(flutterby.grow_and_conquer,2)
##
##
##    badninjas=["Fuma Kotaro"]
##               #"Hittori Hanzo",
##    for ninja in badninjas:
##        temp_ninja=BadNinja(ninja,oval,1)
##        Player.clock.register(temp_ninja.find_and_steal,5)
##
##    trollhunters=["Jack 'o Blades",
##                  "Conan",
##                  "Beowolf",
##                  "Sivard Snarensven"]
##    
##    for hunter in trollhunters:
##        temp_th=TrollHunter(hunter,random.choice(Room.rooms),1)
##        Player.clock.register(temp_th.search_and_destroy,9)
##    
##    homeworks = ['hw-1', 
##                 'hw-2',
##                 'hw-3',
##                 'hw-4',
##                 'hw-5',
##                 'hw-6']
##    
##    for homework in homeworks:
##        Homework(homework,
##                 random.choice(Room.rooms))

    test=Homework('hw-7',oval)
    test.complete()

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

##    for student in students:
##        temp_npc=NPC(student,
##            random.choice(Room.rooms),
##            random.randint(1,5),
##            random.randint(1,5))
##        Player.clock.register(temp_npc.move_and_take_stuff,8)

##    trolls = ['Polyphemus',
##              'Gollum']
##
##    for troll in trolls:
##      tempTroll=Troll(troll,
##            random.choice(Room.rooms),
##            random.randint(1,3),
##            random.randint(1,3))
##      Player.clock.register(tempTroll.eat_people,9)


VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()


SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()
    
    Player.me.look_around()
    Player.clock.register(print_tick_action,10)
    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                
                Player.clock.tick()
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
