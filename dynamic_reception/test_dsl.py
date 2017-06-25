import unittest

from examples.dynamic_reception.builders import PromotionBuilder
from examples.dynamic_reception.semantic_model.base import Route
from examples.dynamic_reception.semantic_model.route_items import Flight, Hotel


class Test(unittest.TestCase):

    def test(self):
        route = Route()
        route.add_item(Flight(source='SVO', destination='AER', airline='Аэрофлот'))
        route.add_item(Hotel(nights=3, brand='Ritsar'))

        builder = PromotionBuilder()
        builder.score(100).when_source('SVO')
        builder.score(500).when_nights(3)

        result = builder.total_score(route)

        self.assertEqual(600, result)
