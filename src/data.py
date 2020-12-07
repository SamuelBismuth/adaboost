class Data:

    def __init__(self, file, delimiter=None):
        with open('/adaboost/data/{0}'.format(file), 'r') as f:
            lines = f.readlines()
            self.lines = []
            for i in range(0, len(lines)):
                data = lines[i].split(delimiter)
                self.fill_line(data)

    
    def print_data(self):
        for line in self.lines:
            print('features: {0}, label: {1}'.format(line.features.get_features(), line.label.get_label()))


class HcBodyTemperature(Data):


    def __init__(self):
        super().__init__('HC_Body_Temperature.txt') 


    def fill_line(self, data):
        self.lines.append(Lines([data[0], data[2]], data[1]))


class Iris(Data):


    def __init__(self):
        super().__init__('iris.data', ',') 


    def fill_line(self, data):
        label = data[4].rstrip()
        if label == 'Iris-setosa':
            return
        self.lines.append(Lines([data[1], data[2]], label))
   


class Lines:


    def __init__(self, features, label):
        self.features = Features(features)
        self.label = Label(label)


class Features:


    def __init__(self, features):
        self.features = features

    
    def get_features(self):
        return self.features


class Label:


    def __init__(self, label):
        self.label = label

    
    def get_label(self):
        if self.label == '1':
            return -1
        elif self.label == '2':
            return 1
        if self.label == 'Iris-virginica':
            return -1
        elif self.label == 'Iris-versicolor':
            return 1