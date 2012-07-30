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

    def __str__(self):
        return "%s (%s, %s)" % (type(self).__name__, str(self.x), str(self.y))


class Line(Geometry):

    def __init__(self, begin, end):
        Geometry.__init__(self)
        self.begin = Point(begin[0], begin[1])
        self.end = Point(end[0], end[1])

    def move(self, x, y):
        self.begin.move(x, y)
        self.end.move(x, y)

    def __str__(self):
        return "%s ((%s, %s), (%s, %s))" % (type(self).__name__,
                str(self.begin.x), str(self.begin.y),
                str(self.end.x), str(self.end.y))


class Polygon(Geometry):

    def __init__(self, point_list, closed=True):
        Geometry.__init__(self)
        self.closed = closed
        self.line_list = self.__create_line_list(point_list)

    def __create_line_list(self, point_list):
        ret = []

        size = len(point_list)
        for i in range(size):
            if i == size - 1 and not self.closed:
                break

            start_point = point_list[i % size]
            end_point = point_list[(i + 1) % size]
            line = Line(start_point, end_point)
            ret.append(line)

        return ret

    def move(self, x, y):
        for l in self.line_list:
            l.move(x, y)

    def __str__(self):
        ret = type(self).__name__ + " (\n"

        size = len(self.line_list)
        for i in range(size):
            line = self.line_list[i]
            ret += "  " + str(line)
            if i < size - 1:
                ret += ", "

            ret += "\n"

        ret += ")"

        return ret

if __name__ == "__main__":
    print Point(0, 0)
    print Line((0, 0), (1, 1))
    print Polygon(((0, 0), (1, 1), (2, 2)))

