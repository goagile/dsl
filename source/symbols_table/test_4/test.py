import unittest

from examples.symbols_table.test_4.units import units


class Test(unittest.TestCase):

    def test(self):
        expected = 'Километры'

        result = units.km.label

        self.assertEqual(expected, result)

    def test_(self):
        expected = 'Километры'

        result = units['km'].label

        self.assertEqual(expected, result)
