from data import HcBodyTemperature, Iris


def print_data(data):
    for data_line in data.data_lines:
        print('features: {0}, label: {1}'.format(data_line.features.get_point().pretty_str(), data_line.label.get_label()))


def print_test_data(data):
    for data_line in data.test_data:
        print('features: {0}, label: {1}'.format(data_line.features.get_point().pretty_str(), data_line.label.get_label()))


def print_train_data(data):
    for data_line in data.train_data:
        print('features: {0}, label: {1}'.format(data_line.features.get_point().pretty_str(), data_line.label.get_label()))


def print_len_test_data(data):
    print(len(data.test_data))


def print_len_train_data(data):
    print(len(data.train_data))
    

hc_body_temperature = HcBodyTemperature()
iris = Iris()

print_data(hc_body_temperature)
print_data(iris)

print('print_len_test_data(hc_body_temperature)')
print_len_test_data(hc_body_temperature)

print('print_test_data(hc_body_temperature)')
print_test_data(hc_body_temperature)

print('print_len_train_data(hc_body_temperature)')
print_len_train_data(hc_body_temperature)

print('print_train_data(hc_body_temperature)')
print_train_data(hc_body_temperature)

print('print_len_test_data(iris)')
print_len_test_data(iris)

print('print_test_data(iris)')
print_test_data(iris)

print('print_len_train_data(iris)')
print_len_train_data(iris)

print('print_train_data(iris)')
print_train_data(iris)