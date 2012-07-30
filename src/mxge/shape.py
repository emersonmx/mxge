import pygame
from constant import *
from geometry import *
from util import *

class Shape(object):
    def __init__(self):
        object.__init__(self)
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
                if intersect_lines(l1.begin, l1.end, l2.begin, l2.end):
                    return True
                vertical_line = (Point(l1.begin.x, l1.begin.y),
                                 Point(l1.begin.x, l1.begin.y + INFINITY_Y))
                if intersect_lines(vertical_line[0],
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
        self.polygon = Polygon(((0, 100), (50, 0), (100, 100)))

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.polygon = Polygon(((0, 0), (25, 0), (25, 25), (0, 25)))

