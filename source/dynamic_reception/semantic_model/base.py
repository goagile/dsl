

class RouteItem:

    def respond_to(self, symbol):
        return hasattr(self, symbol)

    def send(self, symbol):
        return getattr(self, symbol)


class Rule:
    pass


class Condition:
    pass


class Route:

    def __init__(self):
        self.items = []
        self.rules = []

    def add_item(self, item: RouteItem):
        self.items.append(item)

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    def score(self):
        return sum(rule.score_of(self) for rule in self.rules)
