from data import HcBodyTemperature, Iris

hc_body_temperature = HcBodyTemperature()
iris = Iris()

for rule in hc_body_temperature.rules:
    print(rule.line.pretty_str())