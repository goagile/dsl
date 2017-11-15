from examples.dynamic_reception.semantic_model.base import Condition, RouteItem, Route


class EqualityCondition(Condition):
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value

    def match(self, route: Route):
        return any(self.match_item(item) for item in route.items)

    def match_item(self, item: RouteItem):
        if not item.respond_to(self.symbol):
            return False
        return item.send(self.symbol)
