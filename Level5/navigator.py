from waypoint import *
from nav_utils import *


#class for handling navigation algorithms for the characters.
#Is capable of finding shortest paths from one nav node to another.
#Restrictions/Limitations:
#Doesn't account for multiple levels
#Only finds shortest graph path, not euclidian path. Need to add weights to nodes for that.
#Mesh has to be made by hand currently, no auto gen
#No Caching yet.
class Navigator(object):
    @staticmethod
    def dconn(a,b):
        a.conn(b)
        b.conn(a)
    def __init__(self,waypoints):
        self._points=waypoints
    def scale(self,factor):
        for point in self._points:
            point.scale(factor)
    def on_draw(self):
        for point in self._points:
            point.on_draw()

    def pretty_path(self,way1,way2):
        path_point=self.find_path(way1,way2)
        return path_point.path()+[path_point.way()]
            
    def find_path(self,way1,way2):
        pway1=Pathpoint(way1,[])
        return self.find_path_help(pway1,way2,[],[])    

    #to_search is a list of pathpoints
    #searched is a list of pathpoints
    #way1 is a pathpoint
    #way2 is a waypoint
    def find_path_help(self,way1,way2,to_search,searched):
##        print "in:"+ str(way1)
        if way1._way==way2:
            searched.append(way1)
            #return searched for more info perhaps for caching
            return way1
        else:
            to_search.extend(prepare_next(way1,searched))
            next_path=to_search.pop(0)
            searched.append(way1)
            return self.find_path_help(next_path,way2,to_search,searched)
