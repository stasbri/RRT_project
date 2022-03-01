from args import map_size

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{int(self.x)} {int(self.y)}'


def dist(p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


class Map:
    def __init__(self, source):
        if source == "":
            self.size = map_size
            self.start = Point(int(map_size[0] * 0.1), int(map_size[1] * 0.1))
            self.finish = Point(int(map_size[0] * 0.9), int(map_size[1] * 0.9))
        else:
            pass

    def is_way(self, start: Point, end: Point):
        return True


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
        for i in range(len(self.tree)):
            if dist(self.tree[i].point, p) < d:
                d = dist(self.tree[i].point, p)
                best = i
        return self.tree[best]
