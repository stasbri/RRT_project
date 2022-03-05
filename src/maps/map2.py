from .basic_map import BasicMap
# noinspection PyUnresolvedReferences
from geometry import Point
from .map_objects import make_nice_rectangle, make_obstacles_wall_with_hole_in_the_middle_vertical
import random


def second_map():
    resulting_map = BasicMap((1800, 1000))
    resulting_map.start = Point(915, 450)
    resulting_map.finish = Point(1795, 995)
    resulting_map.limit = 50
    for i in range(20, 1800, 50):
        for j in range(0, 1000, 50):

            resulting_map + make_nice_rectangle(i, j, random.randint(10, 40))
    resulting_map.log('src/map_log')
    return resulting_map
