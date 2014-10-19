import random
from npc import *

class BadNinja(NPC):
    def __init__(self,name,loc,restlessness):
        #bad ninjas are dishonorable and almost always steal
        NPC.__init__(self,name,loc,restlessness,1)

    def com_homeworks_around(self):
        to_return=[]
        all_stuff=self.stuff_around()+self.peek_around()
        #print "all_homeworks:"+str(all_homeworks)
        for x in all_stuff :
            if x.is_homework():
                if x.done():
                    to_return.append(x)
        return to_return
    
    def find_and_steal(self,time):
        if not self.is_in_limbo():
            homeworks=self.com_homeworks_around()
            if homeworks:
                self.say("Ooo, that paper looks so interesting!")
                target=random.choice(homeworks)             
                self.location().report(self.name()+' absconds with '+target.name())
                if target.location().is_person():
                    target.location().have_obj_taken(target)
                target.take(self)
                target.destroy()
            else:
                if random.randrange(self._restlessness) == 0:
                    self.move_somewhere()
                else:
                    self.location().report(self.name()+ 'stealthily looks around for things to steal')
                
