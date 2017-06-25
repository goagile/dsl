from examples.dynamic_reception.semantic_model.bonuses import PromotionRule


class PromotionBuilder:

    def __init__(self):
        self.rules = []

    def build_promotion(self):
        return Promotion(self.rules)

    def score(self, value):
        self.rules.append(PromotionRule(score=value))
        return PromotionConditionBuilder(parent=self)


class Promotion:

    def __init__(self, rules):
        self.rules = rules


class PromotionConditionBuilder:

    def __init__(self, parent):
        self.parent = parent
