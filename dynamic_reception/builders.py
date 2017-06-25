from examples.dynamic_reception.semantic_model.base import Route
from examples.dynamic_reception.semantic_model.conditions import EqualityCondition
from examples.dynamic_reception.semantic_model.route_items import Flight, Hotel
from examples.dynamic_reception.semantic_model.rules import PromotionRule


class RouteBuilder:

    def __init__(self):
        self.route = Route()

    def add_flight(self, source, destination, airline):
        self.route.add_item(Flight(source, destination, airline))

    def add_hotel(self, nights, brand):
        self.route.add_item(Hotel(nights, brand))


class PromotionBuilder:

    def __init__(self):
        self.rules = []

    def total_score(self, route):
        route.rules = self.rules
        return route.score()

    def score(self, value):
        rule = PromotionRule(score=value)
        self.rules.append(rule)
        return PromotionConditionBuilder(rule)


class PromotionConditionBuilder:

    def __init__(self, rule: PromotionRule):
        self.rule = rule
        self.symbol = None

    def __getattr__(self, item):
        found = self.__dict__.get(item, None)
        if found:
            return self.__getattribute__(item)
        splitted = item.split('_')
        method = splitted[0]
        self.symbol = splitted[1]
        return self

    def __call__(self, value):
        condition = EqualityCondition(self.symbol, value)
        self.rule.add_condition(condition)
