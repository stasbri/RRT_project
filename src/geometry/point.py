from constants import eps


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{int(self.x)} {int(self.y)}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
