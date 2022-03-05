from .point import Point


class Line:
    def __init__(self, *args, from_points=False):
        if from_points:
            xx = args[1].x - args[0].x
            yy = args[1].y - args[0].y
            self. a = yy
            self.b = xx * (-1)
            self.c = (args[0].x * yy * (-1) + args[0].y * xx)
        else:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]

    def __str__(self):
        return f'{self.a} {self.b} {self.c}'

