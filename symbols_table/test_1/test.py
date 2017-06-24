import unittest

from examples.symbols_table.test_1.units import Units


class Test(unittest.TestCase):

    def test(self):
        expected = 'km'

        result = Units.km

        self.assertEqual(expected, result)
