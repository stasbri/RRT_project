from .line import Line
from .point import Point
from .section import Section
# noinspection PyUnresolvedReferences
from constants import eps


def intersection(l1: Line, l2: Line):
    if not eq(l1.a * l2.b, l2.a * l1.b):
        e = (l1.b * l2.c - l1.c * l2.b) / (l1.a * l2.b - l1.b * l2.a)
        f = (l1.a * l2.c - l1.c * l2.a) / (l1.b * l2.a - l1.a * l2.b)
        return Point(e, f)
    return None


def eq(a, b):
    return (abs(a - b) < eps)


def plus_minus(a):
    if a > 0:
        return 1
    return -1


def point_on_section(p: Point, section: Section):
    start = section.start
    end = section.end
    line = Line(start, end, from_points=True)
    if not eq(start.x * line.a + start.y * line.b + line.c, 0):
        return False
    if min(start.x, end.x) < p.x < max(start.x, end.x) or min(start.y, end.y) < p.y < max(start.y, end.y) or (
                start.x == p.x and start.y == p.y) or (end.x == p.x and end.y == p.y):
        return True
    return False


def ccw(A, B, C):
    if (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x):
        return True
    elif (C.y - A.y) * (B.x - A.x) < (B.y - A.y) * (C.x - A.x):
        return False
    return None


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def intersection_of_sections(s1: Section, s2: Section) -> Point:
    if not intersect(s1.start, s1.end, s2.start, s2.end):
        return s1.end
    int_p = intersection(s1.line, s2.line)
    if int_p is None:
        return s1.end
    if point_on_section(int_p, s1):
        delta_x = plus_minus(int_p.x - s1.start.x) * eps
        delta_y = plus_minus(int_p.y - s1.start.y) * eps
        return Point(int_p.x - delta_x, int_p.y - delta_y)
    return s1.end
