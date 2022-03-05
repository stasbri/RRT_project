from .line import Line
from .point import Point


class Section:
    def __init__(self, p1: Point, p2: Point):
        self.start = p1
        self.end = p2
        self.line = Line(p1, p2, from_points=True)

    def __str__(self):
        return str(self.start) + ' ' + str(self.end)

