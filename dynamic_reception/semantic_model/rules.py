from examples.dynamic_reception.semantic_model.base import Rule, Condition, RouteItem


class PromotionRule(Rule):
    def __init__(self, score):
        self.score = score
        self.conditions = []

    def add_condition(self, condition: Condition):
        self.conditions.append(condition)

    def score_of(self, route: RouteItem):
        all_matches = all(condition.match(route) for condition in self.conditions)
        if not all_matches:
            return 0
        return self.score
