from .basic_map import BasicMap
from .point import Point
from .map_objects import make_nice_square, make_obstacles_wall_with_hole_in_the_middle_vertical
import random
second_map = BasicMap((1800, 1000))
second_map.start = Point(10, 10)
second_map.finish = Point(1795, 995)
second_map.limit = 100
for i in range(20, 1800, 50):
    for j in range(0, 1000, 50):

        second_map + make_nice_square(i, j, random.randint(10, 40))
second_map.log('src/map_log')
