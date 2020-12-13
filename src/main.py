'''
Python version: 3.9
Submitters: Yishay Seroussi 305027948, Samuel Bismuth 342533064.
'''


from data import HcBodyTemperature, Iris
from adaboost import Adaboost


hc_body_temperature = HcBodyTemperature()
iris = Iris()


adaboost_hc_body_temperature = Adaboost(hc_body_temperature.rules, hc_body_temperature.train_data)
adaboost_hc_body_temperature.run_train()
adaboost_hc_body_temperature.print_best_rules('Hc Body Temperature')
hc_body_temperature_train_accuracy = adaboost_hc_body_temperature.get_accuracy(hc_body_temperature.train_data)
hc_body_temperature_test_accuracy = adaboost_hc_body_temperature.get_accuracy(hc_body_temperature.test_data)
print('################# {0} ####################'.format('Hc Body Temperature ACCURACY'))
print('hc body temperature train accuracy: {0}'.format(hc_body_temperature_train_accuracy))
print('hc body temperature test accuracy: {0}'.format(hc_body_temperature_test_accuracy))
print('####################################################')


adaboost_iris = Adaboost(iris.rules, iris.train_data)
adaboost_iris.run_train()
adaboost_iris.print_best_rules('Iris')
iris_train_accuracy = adaboost_iris.get_accuracy(iris.train_data)
iris_test_accuracy = adaboost_iris.get_accuracy(iris.test_data)
print('################# {0} ####################'.format('Iris ACCURACY'))
print('iris train accuracy: {0}'.format(iris_train_accuracy))
print('iris test accuracy: {0}'.format(iris_test_accuracy))
print('####################################################')