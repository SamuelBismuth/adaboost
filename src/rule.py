class Rule:


    def __init__(self, data_lines, line):
        self.line = line
        self.prediction = self.set_prediction(data_lines)


    def set_prediction(self, data_lines):
        sum = 0
        for data_line in data_lines:
            sum += self.line.line.get_relation_point_line(data_line.features.get_point()) * data_line.label.get_label()
        if sum >= 0:
            return 1 
        else:
            return -1


    def predict(self, point):
        if self.line.line.get_relation_point_line(point) >= 0:
            return self.prediction
        else:
            return - self.prediction
    

    def pretty_str(self):
        return '{0}'.format(self.line.line.pretty_str())