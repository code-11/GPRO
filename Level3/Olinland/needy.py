from goalseeker import *

class Needy(GoalSeeking):

    def __init__(self,name,loc,item,desc="This needer has no description"):
        GoalSeeking.__init__(self,name,loc,desc,2)
        self.looking_for=item

    def it(self):
        return self.looking_for

    def item_around(self):
        all_stuff=self.stuff_around()
        for x in all_stuff :
            if x.name()==self.looking_for:
                return x
        return None

    def announce_goal(self):
        self.say("I am looking for "+self.it()+" do you have it?")

    def victory_move(self):
        self.say("oh boy! I found "+self.it()+"! Thats just what I was looking for!")

    def goal_met(self):
        return self.it() in self._inventory

    def goal_move(self,time):
        print "Inventory:"+str(self._inventory)
        item=self.item_around()
        if item:
            item.take(self)
        else:
            self.say("aww nothing interesting here")
            self.move_somewhere()
            
    def have_obj_given(self,obj):
        if obj.name()==self.it():
            self.victory_move()
            self.achieved=True
