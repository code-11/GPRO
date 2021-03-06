from person import *
from clock import *

import sys

class Player (Person):

    # static field representing the player
    me = None
    # static field recording god_mode
    god_mode = False
    # static field representing the clock
    clock = Clock(0)

    def __init__ (self,name,loc):
        Person.__init__(self,name,loc)
        Player.me = self
        self._inventory={}

    # Grab any kind of thing from player's location, 
    # given its name.  The thing may be in the possession of
    # the place, or in the possession of a person at the place.
   
    def thing_named (self,name):
        for x in self.location().contents():
            if x.name() == name:
                return x
        for x in self.peek_around():
            if x.name() == name:
                return x
        return Player.me.inventory().get(name,None)

    def look_around (self):
        def names (lst):
            return ', '.join([x.name() for x in lst])

        loc = self.location()
        exits = loc.exits()
        people = self.people_around()
        all_stuff = self.stuff_around()
        inven=self.inventory().values()

        print '------------------------------------------------------------'
        print 'You are in', loc.name()
        print loc.describe()

        if inven:
            print 'You are carrying:', names(inven)
        else:
            print "You aren't carrying anything"

        if all_stuff:
            print 'You see:', names(all_stuff)
        else: 
            print 'The room is empty'

        if people:
            print 'You see:', names(people)
        else:
            print 'You see no one around'

        if exits:
            print 'Exits:', ', '.join([x for x in exits])
        else:
            print 'There are no exits'
            
##    def add_thing(self,thing):
##        self._inventory[thing.name()]=thing
##    def inventory(self):
##        return self._inventory
    def look_at_object(self,obj):
        print self.name()+" says -- "+obj.description()

#Only the player can win IMO
    def win(self):
        self.say('All my work is done!')
        print 'A winner is you!!! Victorly!!!'
        sys.exit(0)
        
    def die (self):
        self.say('I am slain!')
        Person.die(self)
        print 'This game for you is now over...'
        sys.exit(0)
