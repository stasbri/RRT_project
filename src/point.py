

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{int(self.x)} {int(self.y)}'


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c