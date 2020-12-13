import numpy as np


ITERATIONS = 100
BEST_RULES = 8


class Adaboost:


    def __init__(self, rules, data_lines):
        self.rules = rules
        self.data_lines = data_lines
        self.point_weights = np.full(len(data_lines), 1/len(data_lines))
        self.rules_weigths = np.zeros(len(rules))
        self.rules_error = np.zeros(len(rules))

    
    def run_train(self):
        for i in range(ITERATIONS):
            # 0. Empty errors.
            self.rules_error = np.zeros(len(self.rules))
            # 1. Compute the weighted error for h in H.
            self.compute_weighted_error()
            # 2. Select min weighted error classifier.
            selected_rule = np.argmin(self.rules_error)
            # 3. Set classifier weight.
            self.rules_weigths[selected_rule] = self.compute_rule_weight(selected_rule)
            # 4. Update point weights.
            self.compute_point_weight(selected_rule)

    
    def get_accuracy(self, data):
        best_rules = self.select_best_rules_indexes()
        predicts = np.zeros(len(data))
        for test_data_line_index, test_data_line in enumerate(data):
            rule_sum = 0
            for rule in best_rules:
                rule_sum += self.rules[rule].predict(test_data_line.features.get_point()) * self.rules_weigths[rule]
            if rule_sum >= 0:
                predicts[test_data_line_index] = 1
            else:
                predicts[test_data_line_index] = -1
        print(self.compute_accuracy(predicts, data))
        

    def compute_weighted_error(self):
        for rule_index, rule in enumerate(self.rules):
            for data_line_index, data_line in enumerate(self.data_lines):
                if rule.predict(data_line.features.get_point()) != data_line.label.get_label():
                    self.rules_error[rule_index] += self.point_weights[data_line_index]


    def compute_rule_weight(self, rule_index):
        error = self.rules_error[rule_index]
        return 0.5 * np.log((1 - error) / error)


    def compute_point_weight(self, rule_index):
        for point_weight_index in range(len(self.point_weights)):
            self.point_weights[point_weight_index] *= np.e ** \
            (   - \
                self.rules_weigths[rule_index] * \
                self.rules[rule_index].predict(self.data_lines[point_weight_index].features.get_point()) * \
                self.data_lines[point_weight_index].label.get_label() \
            )
        self.point_weights = np.divide(self.point_weights, np.sum(self.point_weights))

    
    def select_best_rules_indexes(self):
        return self.rules_weigths.argsort()[-BEST_RULES:][::-1] 

    
    def compute_accuracy(self, predicts, data):
        true = 0
        false = 0
        for i in range(len(predicts)):
            if predicts[i] == data[i].label.get_label():
                true += 1
            else:
                false +=1
        return true / len(predicts)