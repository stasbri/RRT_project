import json
import math
from typing import List, Optional, Union
from args import map_size, start, finish
from maps.map_objects import make_obstacles_wall_with_hole_in_the_middle_vertical, \
    make_obstacles_wall_with_hole_in_the_middle_horizontal
import random
from geometry import Point, Section, intersection_of_sections, Obstacle
from maps import all_maps
from logger import testing_logger

tl = testing_logger()


class Map:
    def __init__(self, source=None):
        self.map = source or 'new_map.json'
        f = open(self.map, 'r')
        m: dict = json.loads(f.read())
        f.close()

        self.size: Union[tuple, list] = m['size']
        self.start: Point = Point(*m['start'])
        self.finish: Point = Point(*m['finish'])
        obstacles = list(map(lambda x: Obstacle(list(map(lambda y: Point(*y), x))), m['obstacles']))
        self.obstacles: List[Obstacle] = obstacles
        self.limit = int(m['limit'])

    def new_point(self, start: Point, end: Point) -> Point:
        d = dist(start, end)
        res_p = end
        s = Section(start, res_p)
        for obstacle in self.obstacles:
            tl.log(f'Section : {str(s.start)}, {str(s.end)}')
            tl.log(f'{str(obstacle.max_x)},{str(obstacle.min_x)},{str(obstacle.max_y)},{str(obstacle.min_y)}')
            tl.log(str(obstacle.section_in_checkbox(s)))
            if obstacle.section_in_checkbox(s):
                for section in obstacle.sections:
                    n_p: Point = intersection_of_sections(s, section)
                    if dist(start, n_p) < d:
                        d = dist(start, n_p)
                        res_p = n_p
                        s = Section(start, res_p)
        return res_p

    def is_way(self, start: Point, end: Point):
        for obstacle in self.obstacles:
            if obstacle.section_in_checkbox(Section(start, end)):
                for section in obstacle.sections:
                    if intersect(start, end, section.start, section.end):
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
    def __init__(self, p: Node, limit: int, size: Union[list, tuple]):

        self.size: Optional[list, tuple] = size
        self.root: Node = p
        self.tree: List[List[List[Node]]] = list()
        self.limit = limit
        for i in range(int(size[0] // limit) + 1):
            self.tree.append(list())
            for j in range(int(size[1] // limit) + 1):
                self.tree[i].append(list())

    def add_node(self, n: Node):
        self.tree[int(n.point.x // self.limit)][int(n.point.y // self.limit)].append(n)

    def find_closest_node(self, p: Point):
        d = dist(self.root.point, p)
        best = self.root
        for i in range(len(self.tree)):
            for j in range(len(self.tree[i])):
                for n in self.tree[i][j]:
                    n: Node
                    if dist(n.point, p) < d:
                        d = dist(n.point, p)
                        best = n
        return best

    def close_nodes(self, p: Point) -> List[Node]:
        x = p.x // self.limit
        y = p.y // self.limit
        res = []
        for i in range(int(max(0, x - 1)), int(min(self.size[0], x + 1))):
            for j in range(int(max(0, y - 1)), int(min(self.size[1], y + 1))):
                for n in self.tree[i][j]:
                    if dist(p, n.point) <= self.limit:
                        res.append(n)
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


def ccw(A, B, C) -> Optional[bool]:
    if (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x):
        return True
    elif (C.y - A.y) * (B.x - A.x) < (B.y - A.y) * (C.x - A.x):
        return False
    return None


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
