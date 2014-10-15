from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,desc="This object has no description"):
        Thing.__init__(self,name,loc)
        self._original_location = loc
        self._description=desc

    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc

    def creation_site (self):
        return self._original_location

    def is_mobile_thing (self):
        return True
## Need inventory management    
    def take(self,player):
        self.move(player)
        
    def drop(self,player):
##        del player.inventory()[self.name()]
        self.move(player.location())
        
    def give(self,_from,_to):
        self.move(_to)

