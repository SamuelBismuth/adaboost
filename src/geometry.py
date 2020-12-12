class Point:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def get_x(self):
        return float(self.x)


    def get_y(self):
        return float(self.y)


    def get_point(self):
        return [self.get_x(), self.get_y()] 


    def pretty_str(self):
        return '({0} , {1})'.format(self.get_x(), self.get_y())

    
class Line:


    def __init__(self, point_1, point_2):
        if point_1.get_x() == point_2.get_x():
            self.line = particularLine(point_1.get_x())
        else:
            a = regularLine.get_a_by_points(point_1, point_2)
            b = regularLine.get_b_by_point(point_1, a)
            self.line = regularLine(a, b)
    

class regularLine:


    def __init__(self, a, b):
        self.a = a
        self.b = b

    
    def get_a(self):
        return self.a


    def get_b(self):
        return self.b


    def get_line(self):
        return [self.get_a(), self.get_b()] 


    def pretty_str(self):
        return '{0}x + {1}'.format(self.get_a(), self.get_b())


    def get_relation_point_line(self, point):
        localisation = point.get_x()  * self.get_a() + self.get_b() - point.get_y() 
        if localisation < 0:
            return -1 
        else:
            return 1


    @staticmethod    
    def get_a_by_points(point_1, point_2):
        if point_2.get_x() == point_1.get_x():
            print('ERROR: Check here.')
        return (point_2.get_y() - point_1.get_y()) / (point_2.get_x() - point_1.get_x())


    @staticmethod    
    def get_b_by_point(point_1, a):
        return point_1.get_y() - (a * point_1.get_x())


class particularLine:

    def __init__(self, x):
        self.x = x

    
    def get_x(self):
        return self.x


    def get_line(self):
        return [self.get_x()] 


    def pretty_str(self):
        return 'x = {0}'.format(self.get_x())

    
    def get_relation_point_line(self, point):
        if self.get_x() < point.get_x():
            return -1 
        else:
            return 1