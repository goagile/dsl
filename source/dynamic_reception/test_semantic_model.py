import unittest

from examples.dynamic_reception.semantic_model.rules import PromotionRule
from examples.dynamic_reception.semantic_model.conditions import EqualityCondition
from examples.dynamic_reception.semantic_model.route_items import Flight, Hotel
from examples.dynamic_reception.semantic_model.base import Route


class Test(unittest.TestCase):

    def test(self):
        svo_rule = PromotionRule(score=100)
        svo_rule.add_condition(EqualityCondition('source', 'SVO'))

        n3_rule = PromotionRule(score=300)
        n3_rule.add_condition(EqualityCondition('nights', 3))

        route = Route()
        route.add_item(Flight(source='SVO', destination='AER', airline='Аэрофлот'))
        route.add_item(Hotel(nights=3, brand='Ritsar'))

        route.add_rule(svo_rule)
        route.add_rule(n3_rule)

        result = route.score()

        self.assertEqual(400, result)
