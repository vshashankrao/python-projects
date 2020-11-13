'''
Shashank Rao
RUID: 185005733

'''
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def translate(self, s, t):
        self._x += s
        self._x += t

    def rotate(self, t):
        t = math.radians(t % 360)
        self._x = (self._x * math.cos(t)) - (self._y * math.sin(t))
        self._y = (self._x * math.sin(t)) + (self._y * math.cos(t))
    def distance(self, p):
        d = (((self._x - p._x) ** 2) + ((self._y - p._y) **2) ** .5)
        return d
    def left_of(self, q, r):
        p = self
        diff1 = ((r._x * p._y) - (p._x * r._y))
        diff2 = ((q._x * r._y) - (q._x * p._y))
        diff3 = ((q._y * p._x) - (q._y * r._x))
        return diff1 + diff2 + diff3 > 0

    def right_of(self, q, r):
        p = self
        diff1 = ((r._x * p._y) - (p._x * r._y))
        diff2 = ((q._x * r._y) - (q._x * p._y))
        diff3 = ((q._y * p._x) - (q._y * r._x))
        return diff1 + diff2 + diff3 < 0

    def __str__(self):
        return '(' + str(self._x) + ',' + str(self._y) + ')'
        
    def __repr__(self):
        str(self)

class ConvPoly:
    def __init__(self, *p):
        self._points = list(p)
        self._current = 0
    def translate(self, s, t):
        for point in self._points:
            point = Point.translate(point, s, t)
            

    def rotate(self, t):
        for point in self._points:
            point = Point.rotate(point, t)

    def contains(self, p):
        flag = 0
        for i in range(len(self._points) - 1):
            if not p.left_of(self._points[i], self._points[i + 1]):
                flag = 1
        if not p.left_of(self._points[-1], self._points[0]):
            flag = 1
        return not(bool(flag))

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= len(self._points):
            self._current = 0
            raise StopIteration
        answer = self._points[self._current]
        self._current +=1
        return answer

    def __len__(self):
        return len(self._points)
    
    def __getitem__(self, i):
        if i <0 or i >= len(self):
            raise IndexError
        return self._points[i]
    
    def __str__(self):
        a = []
        for point in self._points:
            a.append(Point.__str__(point))
        return '\n'.join(a)
    
    def __repr__(self):
        return str(self)
    
    def perimeter(self):
        total = self._points[-1].distance(self._points[0])
        for i in range(len(self)-1):
            total += self._points[i].distance(self._points[i+1])
        return total




class Triangle(ConvPoly):

    def __init__(self, p1, p2, p3):
        if not p1.left_of(p2,p3) and not p1.right_of(p2,p3):
            raise Exception("The given points create a straight line")
        else:
            ConvPoly.__init__(self, p1, p2, p3)

    def area(self):
        s = self.perimeter()/2
        a = self._points[0].distance(self._points[1])
        b = self._points[1].distance(self._points[2])
        c = self._points[2].distance(self._points[0])
        area = (s*(s-a)*(s-b)*(s-c)) ** .5
        return area


class EquiTriangle(Triangle):

    def __init__(self, length):
        p1 = Point()
        p2 = Point(length, 0)
        p3 = Point(length/2, length/2*(3**.5))
        Triangle.__init__(self, p1, p2, p3)

        self._length = length

class Rectangle(ConvPoly):

    def __init__(self, length, w):
        p1 = Point()
        p2 = Point(length,0)
        p3 = Point(length,w)
        p4 = Point(0, w)
        ConvPoly.__init__(self, p1,p2,p3,p4)

        self._length = length
        self._width = w

    def area(self):
        return self._length * self._width


class Square(Rectangle):

    def __init__(self, length):
        Rectangle.__init__(self, length, length)


