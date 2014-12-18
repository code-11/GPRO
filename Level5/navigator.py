from waypoint import *
from nav_utils import *
from level_utils import dis, man_dis
import Queue
import random


#class for handling navigation algorithms for the characters.
#Is capable of finding shortest paths from one nav node to another.
#Restrictions/Limitations:
#Doesn't account for multiple levels
#Only finds shortest graph path, not euclidian path. Need to add weights to nodes for that.
#Mesh has to be made by hand currently, no auto gen
#No Caching yet.
class Navigator(object):
    
    #Python has decorators! Who knew!
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
    
    #Finds the distances from all waypoints to a given screen pointt        
    def waypoint_distances(self,x,y,precision=True):
        #Man, dis q is so cool
        dis_q=Queue.PriorityQueue()
        for point in self._points:
            if precision==True:
                the_distance=dis(x,y,point.getX(),point.getY())
            else:
                the_distance=man_dis(x,y,point.getX(),point.getY())
            dis_q.put((the_distance,point))
        return dis_q


    #returns the closes waypoint to a point without checking for a straight line
    #should probably use closest_waypoint in level instead
    def closest_waypoint_abs(self,x,y,precision=True):
        Q=self.waypoint_distances(x,y,precision)
        dis,obj=Q.get()
        return obj

    #returns a random waypoint
    def random_waypoint(self):
        return random.choice(self._points)
    

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
