

class Row:

    def __init__(self, conditions, results):
        self.conditions = conditions
        self.results = results

    def test(self, values):
        return bool(all([
            c.test(v) for c, v in zip(self.conditions, values)
        ]))
