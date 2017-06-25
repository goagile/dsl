import unittest

from examples.dynamic_reception.builders import PromotionBuilder


class Test(unittest.TestCase):

    def test(self):
        builder = PromotionBuilder()
        builder.score(100).when_source('SVO')
        builder.score(300).when_nights(3)

        result = builder.build_promotion()

        self.assertEqual(400, result)
