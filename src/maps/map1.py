from .basic_map import BasicMap
from .point import Point
from .map_objects import make_nice_square, make_obstacles_wall_with_hole_in_the_middle_vertical
first_map = BasicMap((1800, 1000))
first_map.start = Point(10, 10)
first_map.finish = Point(1790, 990)
first_map + make_nice_square(40, 40, 300)
first_map + make_nice_square(350, 350, 300)
first_map + make_nice_square(800, 400, 500)
first_map + make_nice_square(360, 40, 300)
first_map + make_obstacles_wall_with_hole_in_the_middle_vertical(first_map.size, 15)
first_map + make_nice_square(1500, 800, 200)
first_map + make_nice_square(1600, 550, 200)
first_map.limit = 20
first_map.log('src/map_log')
