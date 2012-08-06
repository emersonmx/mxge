import time
from geometry import Point

def ccw(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

def intersect_lines_complex(a, b, c, d):
    den = (d.y - c.y) * (b.x - a.x) - (d.x - c.x) * (b.y - a.y)
    n_a = (d.x - c.x) * (a.y - c.y) - (d.y - c.y) * (a.x - c.x)
    n_b = (b.x - a.x) * (a.y - c.y) - (b.y - a.y) * (a.x - c.x)

    if den == 0:
        return None

    ua = (int(n_a) << 14) / den
    ub = (int(n_b) << 14) / den

    if ua >= 0 and ua <= (1 << 14) and ub >= 0 and ub <= (1 << 14):
        return Point(a.x + (int(ua * (b.x - a.x)) >> 14),
                     a.y + (int(ua * (b.y - a.y)) >> 14))

    return None

def intersect_lines_simple(a, b, c, d):
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

def intersect_lines(a, b, c, d):
    return intersect_lines_complex(a, b, c, d)

