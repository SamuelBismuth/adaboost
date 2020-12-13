from data import HcBodyTemperature, Iris
from adaboost import Adaboost


hc_body_temperature = HcBodyTemperature()
iris = Iris()


adaboost_hc_body_temperature = Adaboost(hc_body_temperature.rules, hc_body_temperature.train_data)
adaboost_hc_body_temperature.run_train()
adaboost_hc_body_temperature.get_accuracy(hc_body_temperature.train_data)
adaboost_hc_body_temperature.get_accuracy(hc_body_temperature.test_data)


adaboost_iris = Adaboost(iris.rules, iris.train_data)
adaboost_iris.run_train()
adaboost_iris.get_accuracy(iris.train_data)
adaboost_iris.get_accuracy(iris.test_data)