import unittest

from examples.symbols_table.test_2.units import units, Keys


class Test(unittest.TestCase):

    def test(self):
        expected = 'Километры'

        result = units[Keys.km].label

        self.assertEqual(expected, result)
