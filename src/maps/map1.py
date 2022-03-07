from .basic_map import BasicMap
# noinspection PyUnresolvedReferences
from geometry import Point
from .map_objects import make_nice_rectangle, make_obstacles_wall_with_hole_in_the_middle_vertical


def first_map():
    resulting_map = BasicMap((1800, 1000))
    resulting_map.start = Point(10, 10)
    resulting_map.finish = Point(1790, 990)
    resulting_map + make_nice_rectangle(40, 40, 300)
    resulting_map + make_nice_rectangle(350, 350, 300)
    resulting_map + make_nice_rectangle(800, 400, 500)
    resulting_map + make_nice_rectangle(360, 40, 300)
    resulting_map + make_obstacles_wall_with_hole_in_the_middle_vertical(resulting_map.size, 15)
    resulting_map + make_nice_rectangle(1500, 800, 200)
    resulting_map + make_nice_rectangle(1600, 550, 200)
    resulting_map.limit = 30
    resulting_map.log('src/map_log')
    return resulting_map
