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
        self.center = self.get_com()

    def get_com(self):
        cmx = (self.p3.x + self.p1.x)/2
        cmy = self.p1.x + (self.p2.y-self.p1.y)/3
        return Point(cmx,cmy)

    def rotate(self, angle: float):
        self.p1.rotate(self.center, angle)
        self.p2.rotate(self.center, angle)
        self.p3.rotate(self.center, angle)


if __name__ == '__main__':
    p1 = Point(-1,-1)
    p2 = Point(0, 2)
    p3 = Point(1, -1)
    pts = [p1,p2,p3]
    tri = Triangle(pts)
    tri.center.print()
    tri.rotate(m.pi/2)
    tri.p2.print()