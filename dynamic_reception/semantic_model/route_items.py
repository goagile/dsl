from examples.dynamic_reception.semantic_model.base import RouteItem


class Flight(RouteItem):
    def __init__(self, source='', destination='', airline=''):
        self.source = source
        self.destination = destination
        self.airline = airline


class Hotel(RouteItem):
    def __init__(self, nights, brand):
        self.nights = nights
        self.brand = brand
