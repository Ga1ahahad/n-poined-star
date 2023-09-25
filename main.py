import math as m


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, origin, angle: float):
        diffx = self.x - origin.x
        diffy = self.y - origin.y
        self.x = diffx * m.cos(angle) - diffy * m.sin(angle) + origin.x
        self.y = diffx * m.sin(angle) + diffy * m.cos(angle) + origin.y

    def print(self):
        print("x: ", self.x, "y: ", self.y)


class Triangle:
    def __init__(self, points: list[Point]):
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]

    def get_com(self):
        cmx = (self.p3.x - self.p1.x)/2
        cmy = self.p2.y/3
        self.com = Point(cmx,cmy)


if __name__ == '__main__':
    p = Point(0, -5)
    p.rotate(Point(0, 0), m.pi/2)
    p.print()