class Geometry(object):
    def __init__(self):
        object.__init__(self)

    def move(self, coordinates):
        pass

class Point(Geometry):
    def __init__(self, x=0, y=0):
        Geometry.__init__(self)
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

class Line(Geometry):
    def __init__(self, begin, end):
        Geometry.__init__(self)
        self.begin = begin
        self.end = end

    def move(self, x, y):
        self.begin.move(x, y)
        self.end.move(x, y)

class Polygon(Geometry):
    def __init__(self, line_list):
        Geometry.__init__(self)
        self.line_list = line_list

    def move(self, x, y):
        for l in self.line_list:
            l.move(x, y)

