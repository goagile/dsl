import unittest


class Test(unittest.TestCase):

    def test_(self):
        PromotionRule(300).hello(32)

    @unittest.skip('')
    def test(self):
        expected = 300
        builder = PromotionBuilder(flight=Flight(source='BOS'))
        builder.score(300).when_from("BOS")

        result = builder.calc_result()

        self.assertEqual(expected, result)


class Flight:
    def __init__(self, source='', destination='', airline=''):
        self.source = source
        self.destination = destination
        self.airline = airline


class PromotionBuilder:

    def __init__(self, flight):
        self._score = 0
        self.flight = flight
        self.rules = []

    def score(self, value):
        rule = PromotionRule(parent=self, value=value)
        self.rules.append(rule)
        return rule

    def calc_result(self):
        for r in self.rules:
            if r.is_ok():
                r.apply()
        return self._score


class PromotionRule(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.condition = None

    def __getattr__(self, condition):
        if not self.__dict__.get(condition, None):
            if condition == 'when_from' or condition == 'hello':
                self.condition = EqualCondition()
            return self
        return self.__getattribute__(condition)

    def __call__(self, value):
        print(value)
        self.condition.value = value

    def is_ok(self):
        return self.condition.is_ok()


class EqualCondition:
    def __init__(self):
        self.value = 0

    def is_ok(self):
        self.value =