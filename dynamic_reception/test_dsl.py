import unittest

from examples.dynamic_reception.builders import PromotionBuilder, RouteBuilder


class Test(unittest.TestCase):

    def test(self):
        person = RouteBuilder()
        person.add_flight(source='SVO', destination='AER', airline='Аэрофлот')
        person.add_hotel(nights=3, brand='Ritsar')

        promotion = PromotionBuilder()
        promotion.score(100).when_source('SVO')
        promotion.score(500).when_nights(3)

        result = promotion.total_score(person.route)

        self.assertEqual(600, result)
