import random
from objects import Point, Map, Node


def random_point_in_range(x_range: tuple, y_range: tuple):
    x = random.uniform(x_range[0], x_range[1])
    y = random.uniform(y_range[0], y_range[1])
    return Point(x, y)


def dist(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def new_point(start: Point, end: Point, limit: float):
    d = dist(start, end)
    if d < limit:
        return end
    x = start.x + (end.x - start.x) * limit/d
    y = start.y + (end.y - start.y) * limit/d
    return Point(x, y)
