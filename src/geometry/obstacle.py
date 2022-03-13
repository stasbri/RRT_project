from typing import List
from .point import Point
from .section import Section
from .functions import intersection_of_sections
from math import inf


class Obstacle:
    def __init__(self, list_of_points: List[Point]):
        self.min_x = inf
        self.min_y = inf
        self.max_x = -inf
        self.max_y = -inf
        self.sections: List[Section] = list()
        self.list = list_of_points
        for i in range(len(list_of_points) - 1):
            if list_of_points[i].x > self.max_x:
                self.max_x = list_of_points[i].x
            if list_of_points[i].x < self.min_x:
                self.min_x = list_of_points[i].x
            if list_of_points[i].y > self.max_y:
                self.max_y = list_of_points[i].y
            if list_of_points[i].y < self.min_y:
                self.min_y = list_of_points[i].y
            self.sections.append(Section(list_of_points[i], list_of_points[i + 1]))
        self.sections.append(Section(list_of_points[-1], list_of_points[0]))
        i = -1
        if list_of_points[i].x > self.max_x:
            self.max_x = list_of_points[i].x
        if list_of_points[i].x < self.min_x:
            self.min_x = list_of_points[i].x
        if list_of_points[i].y > self.max_y:
            self.max_y = list_of_points[i].y
        if list_of_points[i].y < self.min_y:
            self.min_y = list_of_points[i].y
        self.checkbox: List[Section] = list()
        self.checkbox.append(Section(Point(self.max_x, self.max_y), Point(self.max_x, self.min_y)))
        self.checkbox.append(Section(Point(self.max_x, self.max_y), Point(self.min_x, self.max_y)))
        self.checkbox.append(Section(Point(self.min_x, self.min_y), Point(self.max_x, self.min_y)))
        self.checkbox.append(Section(Point(self.min_x, self.min_y), Point(self.min_x, self.max_y)))

    def point_inside(self, p: Point) -> bool:
        if self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y:
            return True
        return False

    def section_in_checkbox(self, s: Section) -> bool:
        if self.point_inside(s.start) or self.point_inside(s.end):
            return True
        for section in self.checkbox:
            if intersection_of_sections(s, section) != s.end:
                return True
        return False

    def enlist(self) -> List[List[float]]:
        res = []
        for section in self.sections:
            res.append([section.start.x, section.start.y])
        return res
