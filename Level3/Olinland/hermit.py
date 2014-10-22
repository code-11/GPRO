from goalseeker import *
class Hermit(GoalSeeking):

    def __init__(self,name,loc,desc="This hermit has no description"):
        GoalSeeking.__init__(self,name,loc,desc,1)
        self._description=desc
        self.time_alone=0

    def goal_move(self,time):
        if not(self.has_achieved()):
            people=self.people_around()
            if people:
                self.complain()
                self.move_somewhere()
                self.time_alone=0
            else:
                self.say("ommm")
                self.time_alone+=1
            
    def announce_goal(self):
        self.say("If you can hear me, get out!")

    def victory_move(self):
        self.say("Enlightenment at last!")
        self._description+=" This hermit is enlightened. You can almost read by the glow!"
        self._name+="-the-enlightened"
    def goal_met(self):
        return self.time_alone==5

    def complain(self):
        self.say("haruumph, why won't people leave me alone?")
