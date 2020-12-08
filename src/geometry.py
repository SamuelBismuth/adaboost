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


    @staticmethod    
    def get_a_by_points(point_1, point_2):
        if point_2.get_x() == point_1.get_x():
            # TODO: Find a solution for the line of the type x = 3.
            return 0
        return (point_2.get_y() - point_1.get_y()) / (point_2.get_x() - point_1.get_x())


    @staticmethod    
    def get_b_by_point(point_1, a):
        return point_1.get_y() - (a * point_1.get_x())