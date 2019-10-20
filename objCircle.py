import sys
class Circle:
    def __init__(self, point, R):
        self.x = point.x
        self.y = point.y
        self.r = int(R)
        self.circle = 2*3.14*self.r 
    def is_point_on_circle(self, point):
        self.a = (self.x - point.x)*(self.x - point.x) + (self.y - point.y)*(self.y - point.y)
        self.b = self.r * self.r
        # print "a",self.a, "b", self.b
        if self.a > self.b:
            print "out"
        elif self.a == self.b:
            print "on"
        else:
            print "in"


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

print "input circle point and R,  x y r"
a = sys.stdin.readline().strip('\n')  
a = a.split()
circlepoint = Point(a[0], a[1])
circle =  Circle(circlepoint, a[2])
while True:
    print "input any point, x y"
    a = sys.stdin.readline().strip('\n')  
    a = a.split()
    anypoint = Point(a[0], a[1])
    circle.is_point_on_circle(anypoint)

