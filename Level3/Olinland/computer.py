import copy
from thing import *


class Computer (Thing):
    def __init__ (self,name,loc):
        Thing.__init__(self,name,loc)
        
    def say (self,msg):
        loc = self.location()
        loc.report(self.name()+'-- '+msg)
        
    def use(self,actor):
        homework=None
        for item in actor.inventory().values():
            if item.is_homework():
                if item.done()==False:
                    homework=item
                    break
        if homework==None:
            actor.say("I don't have any homework to do!")
        elif homework.name().startswith("done"):
            #I think it never gets here now
            #On second thought this is also the wrong way to check for homework completion
            actor.say("This homework is already done!")
        else:
            actor.say('I insert '+homework.name()+' into '+ self.name())
            self.say('Horrible grinding noise')
            self.say('...')
            self.say('Whirr Whirr')
            self.say('...')
            self.say('*Starts overheating*')
            self.say('...')
            self.say('DING!')
            mutible_things_are_weird=copy.copy(homework)
            actor.del_thing(homework)
            mutible_things_are_weird.complete()
            actor.add_thing(mutible_things_are_weird)
            
        
    # FIX ME
