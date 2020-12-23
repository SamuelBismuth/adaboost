'''
Python version: 3.9
Submitters: Yishay Seroussi 305027948, Samuel Bismuth 342533064.
'''


from data import HcBodyTemperature, Iris
from adaboost import Adaboost
import numpy as np


ITERATIONS = 100
BEST_RULES = 8


hc_body_temperature = HcBodyTemperature()
iris = Iris()

total_iris_train_error = np.zeros(BEST_RULES)
total_iris_test_error = np.zeros(BEST_RULES)

total_hc_body_temperature_train_error = np.zeros(BEST_RULES)
total_hc_body_temperature_test_error = np.zeros(BEST_RULES)


for iteration in range(ITERATIONS):

    hc_body_temperature.shuffle_train_test()
    adaboost_hc_body_temperature = Adaboost(hc_body_temperature.rules, hc_body_temperature.train_data)
    adaboost_hc_body_temperature.run_train()
    hc_body_temperature_train_error = adaboost_hc_body_temperature.get_error(hc_body_temperature.train_data)
    hc_body_temperature_test_error = adaboost_hc_body_temperature.get_error(hc_body_temperature.test_data)
    total_hc_body_temperature_train_error = np.add(total_hc_body_temperature_train_error, hc_body_temperature_train_error)
    total_hc_body_temperature_test_error = np.add(total_hc_body_temperature_test_error, hc_body_temperature_test_error)

    iris.shuffle_train_test()
    adaboost_iris = Adaboost(iris.rules, iris.train_data)
    adaboost_iris.run_train()
    iris_train_error = adaboost_iris.get_error(iris.train_data)
    iris_test_error = adaboost_iris.get_error(iris.test_data)
    total_iris_train_error = np.add(total_iris_train_error, iris_train_error)
    total_iris_test_error = np.add(total_iris_test_error, iris_test_error)


for i in range(BEST_RULES):

    print('################# {0} ####################'.format('Hc Body Temperature error'))
    print('hc body temperature train error: {0}'.format(np.divide(total_hc_body_temperature_train_error, 100)[i]))
    print('hc body temperature test error: {0}'.format(np.divide(total_hc_body_temperature_test_error, 100)[i]))
    print('####################################################')

    print('################# {0} ####################'.format('Iris error'))
    print('iris train error: {0}'.format(np.divide(total_iris_train_error, 100)[i]))
    print('iris test error: {0}'.format(np.divide(total_iris_test_error, 100)[i]))
    print('####################################################')