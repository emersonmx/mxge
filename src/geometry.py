class Geometry:
    def move(self, coordinates):
        pass

class Point(Geometry):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

class Line(Geometry):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def move(self, x, y):
        self.begin.move(x, y)
        self.end.move(x, y)

class Polygon(Geometry):
    def __init__(self, line_list):
        self.line_list = line_list

    def move(self, x, y):
        for l in self.line_list:
            l.move(x, y)

