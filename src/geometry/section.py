from .line import Line
from .point import Point


def dist(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


class Section:
    def __init__(self, p1: Point, p2: Point):
        self.start = p1
        self.end = p2
        self.line = Line(p1, p2, from_points=True)

    def __str__(self):
        return str(self.start) + ' ' + str(self.end)

    def __le__(self, other):
        return dist(self.start, self.end) <= dist(other.start, other.end)

    def __lt__(self, other):
        return dist(self.start, self.end) < dist(other.start, other.end)
