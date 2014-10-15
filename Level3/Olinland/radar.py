from mobile import *
from room import *


class Radar (MobileThing):

#Since you're not adding anthing here, its better to just allow the super constructor free reign
##    def __init__ (self,name,loc):
##        MobileThing.__init__(self,name,loc)

    def display_room_contents(self,actor,room):
        for content in room.contents():
            actor.say("I detect "+content.name()+" in "+room.name())

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        if self.location()==Player.me:
            self.recurse(actor,[Player.me.location()],[])
        else:
            self.recurse(actor,[self.location()],[])
        
    def recurse(self,actor,rooms_to_explore,seen_rooms):
        if rooms_to_explore!=[]:
            a_room=rooms_to_explore.pop()
            #print type(a_room)
            seen_rooms.append(a_room)
            self.display_room_contents(actor,a_room)
            
            for adjacent in a_room.exits().values():
                if not(adjacent in seen_rooms):
                    rooms_to_explore.append(adjacent)

            self.recurse(actor,rooms_to_explore,seen_rooms)
            

        #actor.say(str(self.location().contents()))
        # FIX ME
        #actor.say("Mmm. It looks like it's broken...")
        
