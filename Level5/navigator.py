from waypoint import *
class Navigator(object):
    def __init__(self,waypoints):
        self._points=waypoints
    def scale(self,factor):
        for point in self._points:
            point.scale(factor)
    def on_draw(self):
        for point in self._points:
            point.on_draw()
