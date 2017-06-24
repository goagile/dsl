import unittest
from datetime import date, time

from examples.expression_builder.calendar_model import Event
from examples.expression_builder.script import calendar


class TestCalendar(unittest.TestCase):

    def test(self):
        expected = Event('Domain Specific Language tutorial')
        expected._date = date(2017, 1, 1)
        expected._start = time(10, 0)
        expected._end = time(11, 0)
        expected._place = 'Developers Office'

        result = calendar.events[0]

        self.assertEqual(expected, result)
