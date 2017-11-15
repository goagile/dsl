import unittest

from examples.symbols_table.test_3.units import units, Keys


class Test(unittest.TestCase):

    def test(self):
        expected = 'Километры'

        result = units.km.label

        self.assertEqual(expected, result)
