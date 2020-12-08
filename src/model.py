from geometry import Point


class DataLine:


    def __init__(self, features, label):
        self.features = Features(features)
        self.label = Label(label)


class Features:


    def __init__(self, features):
        self.features = Point(features[0], features[1]) 


    def get_point(self):
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