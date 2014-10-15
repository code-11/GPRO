import sys
from webbrowser import open_new
from player import *

SAME_ROUND = 1
NEXT_ROUND = 2  

class Verb (object):

    def act (self,input):
        if len(input)==0:
            return self.action0()
        if len(input)==1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print 'Word',input[0],'not understood'
                return SAME_ROUND
            return self.action1(wo1)
        if len(input)>1:
            wo1 = Player.me.thing_named(input[0])
            if wo1 is None:
                print 'Word',input[0],'not understood'
                return SAME_ROUND
            wo2 = Player.me.thing_named(input[1])
            if wo2 is None:
                print 'Word',input[1],'not understood'
                return SAME_ROUND
            return self.action2(wo1,wo2)

    def action0 (self):
        print 'Input not understood'
        return SAME_ROUND

    def action1 (self,wo1):
        print 'Input not understood'
        return SAME_ROUND

    def action2 (self,wo1,wo2):
        print 'Input not understood'
        return SAME_ROUND



class Quit (Verb):

    def action0 (self):
        print 'Goodbye'
        sys.exit(0)


class Direction (Verb):
    def __init__ (self,dir):
        self._direction = dir

    def action0 (self):
        if Player.me.go(self._direction):
            return NEXT_ROUND
        else:
            return SAME_ROUND


class Look (Verb):

    def action0 (self):
        Player.me.look_around()
        return SAME_ROUND

    def action1 (self,obj):
        Player.me.look_at_object(obj)


class Wait (Verb):

    def action0 (self):
        return NEXT_ROUND

class God (Verb):

    def action0 (self):
        if Player.god_mode:
            Player.god_mode = False
        else:
            Player.god_mode = True
        print '(God mode is now','on)' if Player.god_mode else 'off)'
        return SAME_ROUND


class Use (Verb):

    def action1 (self,obj):
        obj.use(Player.me)
        return SAME_ROUND



class Take (Verb):

    def action1 (self,obj):
        if obj.location()==Player.me:
            Player.me.say('I already have the '+obj.name()+' but I guess I could USE it')
        else:
            if not(obj.is_person()):
                Player.me.say('I take the '+obj.name()+" from "+obj.location().name())
            elif obj==Player.me:
                print "This calls for some music!"
                open_new("http://youtu.be/djV11Xbc914?t=53s")
            if obj.location().is_person() and not(obj.location()==Player.me):
                obj.location().have_obj_taken(obj)
            obj.take(Player.me)
        return SAME_ROUND

class Drop (Verb):

    def action1 (self,obj):
        if not Player.me.have_thing(obj):
            Player.me.say('I am not carrying '+obj.name())
        else:
            Player.me.say('I drop the '+obj.name())
            obj.drop(Player.me)
        return SAME_ROUND

class Give (Verb):

    def action2 (self,obj1,obj2):
        Player.me.say('I reluctantly give the '+obj1.name()+' to '+obj2.name())
        obj2.have_obj_given(obj1)
        obj1.give(Player.me,obj2)
        return SAME_ROUND

        
