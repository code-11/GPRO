import random
from person import *
# A butterfly is person because I wanted the movement methods
# Mabye I should have used composition, but 
class ButterFly(Person):
    #state is either CATERPILLAR,COCOON, BUTTERFLY or MOTHRA
    stage1=2
    stage2=4
    stage3=100
    
    def __init__(self,name,loc,desc="This object has no description"):
        Person.__init__(self,name,loc,desc)
        self.state="CATERPILLAR"
        self.age=0
        self._description="It is a caterpillar"
    
    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)

    def report_state(self):
        if not(self.location().is_person()):
            self.location().report(self.name() + " has grown to a "+self.state.lower())
        else:
            print self.name() + " has grown to a "+self.state.lower()
            
    def this_isnt_even_my_true_form(self):
        if self.state=="CATERPILLAR":
            self.state="COCOON"
        elif self.state=="COCOON":
            self.state="BUTTERFLY"
        elif self.state=="BUTTERFLY":
            self.state="MOTHRA"
        else:
            print "Butterfly has malfunctioned, bring it to a certified, licensed buterfly dealer"
        self.report_state()
        self._description="It is a "+self.state.lower()
    def sanity_check(self):
        print "in sanity check"
        if not(self.location().is_room()):
            print "in if"
            self.move(self.location().location())

    def grow(self):
        if self.age==ButterFly.stage1:
            self.this_isnt_even_my_true_form()
        elif self.age==ButterFly.stage2:
            self.sanity_check()
            self.this_isnt_even_my_true_form()
        elif self.age==ButterFly.stage3:
            self.this_isnt_even_my_true_form()
        self.age+=1

    def conquer(self):
        if not(self.state=="CATERPILLAR" or self.state=="COCOON"):
            self.move_somewhere()

    def grow_and_conquer(self,time):
        self.grow()
        self.conquer()

    def move (self,loc):
        if self.state=="CATERPILLAR" or self.state=="COCOON":
            self.location().del_thing(self)
            loc.add_thing(self)
            self._location = loc
        else:
            print "Something has gone horribly wrong"

    def take(self,player):
        if self.state=="CATERPILLAR" or self.state=="COCOON":
            self.move(player)
        else:
            player.say('I try to take '+self.name()+' but it gracefully avoids my clumsy hands')

    def drop(self,player):
        if self.state=="CATERPILLAR" or self.state=="COCOON":
            self.move(player.location())
        else:
            print actor.name(),'is not carrying',self.name()

    def give(self,player,target):
        if self.state=="CATERPILLAR" or self.state=="COCOON":
            self.move(target)
        else:
            print actor.name(),'is not carrying',self.name()

    def is_person(self):
        return False

        
