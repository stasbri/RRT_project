from typing import List
from .point import Point


def make_obstacles_wall_with_hole_in_the_middle_vertical(field_size: tuple, hole_size: int):
    x = field_size[0] // 2
    y1 = 0
    y2 = int(field_size[1] * (0.5 - hole_size/100))
    y3 = int(field_size[1] * (0.5 + hole_size/100))
    y4 = field_size[1]
    p1 = Point(x, y1)
    p2 = Point(x, y2)
    p3 = Point(x, y3)
    p4 = Point(x, y4)
    return [[p1, p2], [p3, p4]]


def make_obstacles_wall_with_hole_in_the_middle_horizontal(field_size: tuple, hole_size: int):
    y = field_size[1] // 2
    x1 = 0
    x2 = int(field_size[0] * (0.5 - hole_size/100))
    x3 = int(field_size[0] * (0.5 + hole_size/100))
    x4 = field_size[0]
    p1 = Point(x1, y)
    p2 = Point(x2, y)
    p3 = Point(x3, y)
    p4 = Point(x4, y)
    return [[p1, p2], [p3, p4]]


def make_nice_square(left_cor: int, up_cor: int, side_length: int):
    res: List[List[Point]] = []
    x = left_cor
    y = up_cor
    p1 = Point(x, y)
    p2 = Point(x + side_length, y)
    p3 = Point(x + side_length, y + side_length)
    p4 = Point(x, y + side_length)
    res.append([p1, p2])
    res.append([p2, p3])
    res.append([p3, p4])
    res.append([p4, p1])
    return res
