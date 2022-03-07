from typing import List
from args import map_size, start, finish
from maps.map_objects import make_obstacles_wall_with_hole_in_the_middle_vertical, \
    make_obstacles_wall_with_hole_in_the_middle_horizontal
import random
from geometry import Point, Section, intersection_of_sections
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
            m = all_maps[source]()
            self.size: tuple = m.size
            self.start: Point = m.start
            self.finish: Point = m.finish
            self.obstacles: List[list] = m.obstacles
            self.limit = m.limit

    def new_point(self, start: Point, end: Point) -> Point:
        d = dist(start, end)
        res_p = end
        for i in range(len(self.obstacles)):
            n_p: Point = intersection_of_sections(Section(start, res_p),
                                                  Section(self.obstacles[i][0], self.obstacles[i][1]))
            if dist(start, n_p) < d:
                d = dist(start, n_p)
                res_p = n_p
        return res_p

    def is_way(self, start: Point, end: Point):
        for i in range(len(self.obstacles)):
            if intersect(start, end, self.obstacles[i][0], self.obstacles[i][1]):
                return False
        return True

    def random_point_in_range(self):
        r = random.randint(1, 10)
        if r:
            x = random.uniform(0, self.size[0])
            y = random.uniform(0, self.size[1])
        else:
            x = random.uniform(max(0, self.finish.x - self.limit), min(self.size[0], self.finish.x + self.limit))
            y = random.uniform(max(0, self.finish.y - self.limit), min(self.size[1], self.finish.y + self.limit))
        return Point(x, y)

    def dump(self):
        pass


class Node:
    def __init__(self, p: Point, ans=None):
        self.point = p
        self.ans: Node = ans

    def cost(self):
        if self.ans is None:
            return 0
        return dist(self.point, self.ans.point) + self.ans.cost()


class Tree:
    def __init__(self, p: Node):
        self.root: Node = p
        self.tree: List[Node] = [p]

    def add_node(self, n: Node):
        self.tree.append(n)

    def find_closest_node(self, p: Point):
        d = dist(self.tree[0].point, p)
        best = 0
        for i in range(len(self.tree)):
            if dist(self.tree[i].point, p) < d:
                d = dist(self.tree[i].point, p)
                best = i
        return self.tree[best]

    def close_nodes(self, p: Point, limit) -> List[Node]:
        res = []
        for node in self.tree:
            if dist(node.point, p) <= limit:
                res.append(node)
        return res


# here we go with functions



def dist(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def new_point(start: Point, end: Point, limit: float) -> Point:
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
