from typing import Optional
import math
from . import Point
from .line import Line
from .point import Point
from .section import Section
# noinspection PyUnresolvedReferences
from constants import eps


def dist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def intersection(l1: Line, l2: Line) -> Optional[Point]:
    if not eq(l1.a * l2.b, l2.a * l1.b):
        e = (l1.b * l2.c - l1.c * l2.b) / (l1.a * l2.b - l1.b * l2.a)
        f = (l1.c * l2.a - l2.c * l1.a) / (l1.a * l2.b - l1.b * l2.a)
        return Point(e, f)
    return None


def eq(a, b):
    return (abs(a - b) < eps)


def plus_minus(a) -> int:
    if a > 0:
        return 1
    return -1


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
    if not intersect(s1.start, s1.end, s2.start, s2.end):
        return s1.end
    int_p = intersection(s1.line, s2.line)
    start = s1.start
    if int_p is None:
        return s1.end
    if point_on_section(int_p, s1):
        delta_x = int_p.x - s1.start.x
        delta_y = int_p.y - s1.start.y
        delta_x *= (delta_x ** 2 >= 1)
        delta_y *= (delta_y ** 2 >= 1)
        return Point(start.x + delta_x * (1 - 10 * eps), start.y + delta_y * (1 - 10 * eps))
    return s1.end
