#! /usr/bin/env python

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def ah(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

def intersect(a, b, c, d):
    return ah(a, c, d) != ah(b, c, d) and ah(a, b, c) != ah(a, b, d)

def main():
    a = Ponto(3,5)
    b = Ponto(6,2)
    c = Ponto(2,1)
    d = Ponto(7,6)

    print intersect(a, b, c, d)

if __name__ == "__main__":
    main()
