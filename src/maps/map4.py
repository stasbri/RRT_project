from .basic_map import BasicMap
# noinspection PyUnresolvedReferences
from geometry import Point
from .map_objects import make_nice_rectangle, make_obstacles_wall_with_hole_in_the_middle_vertical


def fourth_map():
    resulting_map = BasicMap((900, 500))
    resulting_map.start = Point(10, 10)
    resulting_map.finish = Point(890, 490)
    resulting_map + make_obstacles_wall_with_hole_in_the_middle_vertical(resulting_map.size, 50)
    resulting_map.limit = 10
    resulting_map.log('src/map_log')
    return resulting_map
