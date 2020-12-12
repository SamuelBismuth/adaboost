from data import HcBodyTemperature, Iris
from adaboost import Adaboost

hc_body_temperature = HcBodyTemperature()
iris = Iris()


adaboost_hc_body_temperature = Adaboost(hc_body_temperature.rules, hc_body_temperature.train_data)
adaboost_iris = Adaboost(iris.rules, iris.train_data)

# adaboost_hc_body_temperature.run()
adaboost_iris.run()

for rule_weight in adaboost_iris.rules_weigths:
    print(rule_weight)