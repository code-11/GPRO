import random
from player import *
from person import *

# A goal seeker is a NPC who through the use of its goal move,
# ries to fill some objective.
class GoalSeeking(Person):

    def __init__(self,name,loc,desc="This goalseeker has no description",importance=9):
        Person.__init__(self,name,loc,desc)
        self._description=desc
        self.achieved=False
        Player.clock.register(self.packaged_move,importance)

    #one registered function is easier to deal with than many
    def packaged_move(self,time):
        self.goal_move(time)
        if self.goal_met() and self.achieved==False:
            self.victory_move()
            self.achieved=True
            #ideally it would unsubscribe the goal move here

    #Special registered move that the npc tries to fufill
    #Theoretically this move should increment the goalseeker closerr to its goal each round
    def goal_move(self,time):
        print "This function should be overriden"
    
    #Has the NPC acheived its goal?
    def has_achieved(self):
        return self.achieved

    #What to do whan you complete the goal
    def victory_move(self):
        print "This function should be overriden"

    def announce_goal(self):
        print "This function should be overriden"
        
    #Some test to determine whether the NPC has met their goal
    def goal_met(self):
        print "This function should be overriden"
        return False

    #Lazy. Should really reorganize inheritance tree
    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)
