from wobject import *
from player import *


class Room (WObject): #,Container):

    rooms = []

    def __init__ (self,name,desc="This room has no description"):
        WObject.__init__(self,name)
        self._exits = {}
        self._contents = []
        self._description=desc
        Room.rooms.append(self)

    def exits (self):
        return self._exits

    def contents (self):
        return self._contents

    # You see room reports only if you are in the same room
    # or if you have enabled god mode

    def report (self,msg):
        if Player.me.location() is self:
            print msg
        elif Player.god_mode:
            print '(At', self.name(), msg+')'
    def describe(self):
        return self._description

    def broadcast (self,msg):
        print msg

    def is_room (self):
        return True


    def have_thing (self,t):
        for c in self.contents():
            if c is t:
                return True
        return False

    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]
