from waypoint import *
class Navigator(object):
    def __init__(self,waypoints):
        self._points=waypoints
    def scale(self,factor):
        for point in self._points:
            point.scale(factor)
