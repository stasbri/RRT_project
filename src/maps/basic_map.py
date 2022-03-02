from typing import List, Tuple
from .point import Point
import os


class BasicMap:
    def __init__(self, size: tuple):
        self.obstacles: List[Tuple[Point]] = []
        self.start: Point = None
        self.finish: Point = None
        self.size: tuple = size
        self.limit = 10

    def __add__(self, other: List[Tuple[Point]]):
        self.obstacles += other

    def log(self, file_name: str = 'map_log'):
        os.system(f'rm {file_name}')
        for i in range(len(self.obstacles)):
            s = str(self.obstacles[i][0])
            s += ' ' + str(self.obstacles[i][1])
            os.system(f'echo {s} >> {file_name}')
