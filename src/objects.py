from typing import List
from args import map_size, start, finish
from maps.map_objects import make_obstacles_wall_with_hole_in_the_middle_vertical, \
    make_obstacles_wall_with_hole_in_the_middle_horizontal
import random
from point import Point
from maps import all_maps


class Map:
    def __init__(self, source):
        if source is None:
            self.size: tuple = map_size
            self.start: Point = start
            self.finish: Point = finish
            self.obstacles: List[list] = make_obstacles_wall_with_hole_in_the_middle_vertical(map_size, 5) \
                                         + make_obstacles_wall_with_hole_in_the_middle_horizontal(map_size, 5)
            self.limit = 10
        else:
            m = all_maps[source]
            self.size: tuple = m.size
            self.start: Point = m.start
            self.finish: Point = m.finish
            self.obstacles: List[list] = m.obstacles
            self.limit = m.limit

    def is_way(self, start: Point, end: Point):
        for i in range(len(self.obstacles)):
            if intersect(start, end, self.obstacles[i][0], self.obstacles[i][1]):
                return False
        return True

    def dump(self):
        pass


class Node:
    def __init__(self, p: Point, ans=None):
        self.point = p
        self.ans: Node = ans


class Tree:
    def __init__(self, p: Node):
        self.root = p
        self.tree = [p]

    def add_node(self, n: Node):
        self.tree.append(n)

    def find_closest_node(self, p: Point):
        d = dist(self.tree[0].point, p)
        best = 0
        second_best = 0
        for i in range(len(self.tree)):
            if dist(self.tree[i].point, p) < d:
                d = dist(self.tree[i].point, p)
                second_best = best
                best = i
        return self.tree[best], self.tree[second_best]


# here we go with functions

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
    x = start.x + (end.x - start.x) * limit / d
    y = start.y + (end.y - start.y) * limit / d
    return Point(x, y)


def dist(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def ccw(A, B, C):
    if (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x):
        return True
    elif (C.y - A.y) * (B.x - A.x) < (B.y - A.y) * (C.x - A.x):
        return False
    return None


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
