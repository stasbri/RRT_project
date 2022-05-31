from typing import Optional
import math
from . import Point
from .line import Line
from .point import Point
from .section import Section
# noinspection PyUnresolvedReferences
from constants import eps, understep


def dist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def intersection(l1: Line, l2: Line) -> Optional[Point]:
    if not eq(l1.a * l2.b, l2.a * l1.b):
        e = (l1.b * l2.c - l1.c * l2.b) / (l1.a * l2.b - l1.b * l2.a)
        f = (l1.c * l2.a - l2.c * l1.a) / (l1.a * l2.b - l1.b * l2.a)
        return Point(e, f)
    return None


def normal_to_line(point, line):
    x = point.x
    y = point.y
    a = line.b
    b = line.a * (-1)
    c = line.a * y - a * x
    return Line(a, b, c)


def eq(a, b):
    return (abs(a - b) < eps)


def plus_minus(a) -> int:
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return 0

def point_on_section(p: Point, section: Section) -> bool:
    start = section.start
    end = section.end
    line = Line(start, end, from_points=True)
    if not eq(start.x * line.a + start.y * line.b + line.c, 0):
        return False
    if min(start.x, end.x) < p.x < max(start.x, end.x) or min(start.y, end.y) < p.y < max(start.y, end.y) or (
                start.x == p.x and start.y == p.y) or (end.x == p.x and end.y == p.y):
        return True
    return False


def ccw(A: Point, B: Point, C: Point):
    if (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x):
        return True
    elif (C.y - A.y) * (B.x - A.x) < (B.y - A.y) * (C.x - A.x):
        return False
    return None


def intersect(A: Point, B: Point, C: Point, D: Point):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def intersection_of_sections(s1: Section, s2: Section) -> Point:
    if intersect(s1.start, s1.end, s2.start, s2.end) is False:
        return s1.end
    int_p = intersection(s1.line, s2.line)
    start = s1.start
    if int_p is None:
        return s1.end
    if point_on_section(int_p, s1) and point_on_section(int_p, s2):
        l = normal_to_line(int_p, s2.line)
        if l.b == 0:
            y1 = int_p.y + 1
            y2 = int_p.y - 1
            x1 = -(l.c + l.b * y1) / l.a
            x2 = -(l.c + l.b * y2) / l.a
        else:
            x1 = int_p.x + 1
            x2 = int_p.x - 1
            y1 = -(l.c + l.a * x1) / l.b
            y2 = -(l.c + l.a * x2) / l.b


        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        if dist(start, p1) < dist(start, p2):
            return p1
        else:
            return p2
    return s1.end
