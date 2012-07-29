import pygame
from type import *
from geometry import *

def ccw(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

def intersect(a, b, c, d):
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

class Shape:
    def __init__(self):
        self.line_list = []
        self.polygon = None
        self.color = (0, 0, 0)

    def move(self, x, y):
        self.polygon.move(x, y)

    def draw(self, surface):
        for l in self.polygon.line_list:
            pygame.draw.line(surface,
                             self.color,
                             (l.begin.x, l.begin.y),
                             (l.end.x, l.end.y))

    def collide(self, geometry):
        for l1 in self.polygon.line_list:
            count = 0
            for l2 in geometry.polygon.line_list:
                if intersect(l1.begin, l1.end, l2.begin, l2.end):
                    return True
                vertical_line = (Point(l1.begin.x, l1.begin.y),
                                 Point(l1.begin.x, l1.begin.y + INFINITY_Y))
                if intersect(vertical_line[0],
                             vertical_line[1],
                             l2.begin,
                             l2.end):
                    count += 1

            if count % 2 == 1:
                return True

        return False

class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.line_list = (
            Line(Point(0, 100), Point(50, 0)),
            Line(Point(50, 0), Point(100, 100)),
            Line(Point(100, 100), Point(0, 100))
        )
        self.polygon = Polygon(self.line_list)

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.line_list = (
            Line(Point(0, 0), Point(25, 0)),
            Line(Point(25, 0), Point(25, 25)),
            Line(Point(25, 25), Point(0, 25)),
            Line(Point(0, 25), Point(0, 0))
        )
        self.polygon = Polygon(self.line_list)

