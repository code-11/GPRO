import random
from npc import *
class TrollHunter(NPC):

    def __init__(self,name,loc,restlessness):
        #troll hunters are an honorable lot and thus almost never steal.
        #miserly trait not required as an input
        NPC.__init__(self,name,loc,restlessness,1000)

    def search_and_destroy(self,time):
        if not self.is_in_limbo():
            trolls=self.trolls_around()
            # Troll hunters will stay in the room until the troll leaves or are dead
            # Troll hunters are persistent!
            if trolls:
                self.say("Trollago delenda est!")
                blaggard=random.choice(trolls)
                self.location().report(self.name()+ 'heaves his weapon at '+blaggard.name())
                blaggard.suffer(random.randint(1,4))
            else:
                self.say("Alas, my abilities are needed elsewhere!")
                self.move_somewhere()    

    def trolls_around(self):
        return [x for x in self.location().contents()
                if x.is_troll() and x is not self]
    
            
