from model import DataLine, Point
from geometry import Line
from rule import Rule
import random


class Data:


    def __init__(self, file, delimiter=None):
        with open('/adaboost/data/{0}'.format(file), 'r') as f:
            file_lines = f.readlines()
            self.data_lines = []
            self.rules = []
            for i in range(0, len(file_lines)):
                data = file_lines[i].split(delimiter)
                self.fill_data_line(data)
            random.shuffle(self.data_lines)
            middle = int(len(self.data_lines) / 2)
            self.test_data = self.data_lines[:middle]       
            self.train_data = self.data_lines[middle:]
            self.set_rules()


    def set_rules(self):
        for i in range(0, len(self.data_lines)):
            for j in range(i + 1, len(self.data_lines)):
                point_1 = self.data_lines[i].features.get_point()
                point_2 = self.data_lines[j].features.get_point()
                self.rules.append(Rule(self.data_lines, Line(point_1, point_2)))  # TODO: Check if we don't send all the train_data.


class HcBodyTemperature(Data):


    def __init__(self):
        super().__init__('HC_Body_Temperature.txt') 
        

    def fill_data_line(self, data):
        self.data_lines.append(DataLine([data[0], data[2]], data[1]))


class Iris(Data):


    def __init__(self):
        super().__init__('iris.data', ',') 


    def fill_data_line(self, data):
        label = data[4].rstrip()
        if label == 'Iris-setosa':
            return
        self.data_lines.append(DataLine([data[1], data[2]], label))