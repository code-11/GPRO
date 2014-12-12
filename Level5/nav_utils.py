class Pathpoint(object):
    def __init__(self,waypoint,path):
        self._way=waypoint
        self._path=path
        self._name=self._way._name
    def way(self):
        return self._way
    def points(self):
        return self._way._points
    def path(self):
        return self._path
    def __repr__(self):
        path_str=""
        for point in self._path:
            path_str+=point.__repr__()+","
        return "("+self._name+",["+path_str+"])"

#gets all waypoint from a list of path points.
#ppoint_list=[path]
def get_waypoints(ppoint_list):
    to_return=[]
    for ppoint in ppoint_list:
##        print type(ppoint)
        to_return.append(ppoint.way())
    return to_return

#checks a list of waypoints against a list of seen pathpoints
#The path doesn't matter in the comparison, only the waypoint.
#the_list=[way] seen=[path]
def unseen_only(the_list,seen):
    to_return=[]
    seen_waypoints=get_waypoints(seen)
    for point in the_list:
        if not(point in seen_waypoints):
            to_return.append(point)
    return to_return

#promotes children waypoints to children pathpoints preserving path of parent. 
#parent=path children=[way]
def promote(parent,children):
    to_return=[]
    for child in children:
        to_return.append(Pathpoint(child,parent.path()+[parent.way()]))
    return to_return

#returns a list of unseen child path points
def prepare_next(path_point,searched):
    points=path_point.points()
    #get all unseen waypoint children
    unseen=unseen_only(points,searched)
    #make them into pathpoints
    child_paths=promote(path_point,unseen)
    return child_paths
