

class DecisionTable:

    def __init__(self):
        self.rows = []

    def calc(self, values):
        results = self.get_results(values)
        return [r.calc() for r in results]

    def get_results(self, values):
        if not self.rows:
            raise ValueError('Rows is Empty')

        for row in self.rows:
            if row.test(values):
                return row.results

        raise ValueError('No one rows has True test')
