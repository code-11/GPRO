from player import *
from npc import *
import random

class Professor (NPC):

      def __init__ (self,name,loc,restlessness,professorial):
      	  NPC.__init__(self,name,loc,restlessness,100)
          self._professorial = professorial

      _topics = ['Turing machines',
                 'the lambda calculus',
                 'Godel']

      def lecture (self,time):
        if not self.is_in_limbo():
          if random.randrange(self._professorial) == 0:
              if self.people_around():
                  self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
              else:
                  self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))
      def have_obj_given(self,obj):
            if obj.is_homework():
                  if obj.done():
                        self.say("Looks good!")
                        Player.me.win()
                  else:
                        # Something is borked with this branch
                        # The homework is lost, probably due to lack of implementation of person container
                        # In the spirit of early games, masking technical difficulties with story!
                        print self.name()+" absent mindedly brushes the incomplete "+obj.name()+" to the ground"
                        print "A grue eats the succulent assignment"
            else:
                  self.say("Thanks for the "+obj.name()+"!")
