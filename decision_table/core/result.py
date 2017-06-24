

class Result:

    def __init__(self, arg):
        self.arg = arg

    def calc(self):
        return self.arg

    def __eq__(self, other):
        return bool(self.arg == other.arg)
