

class IsNone:

    def test(self, arg):
        return bool(arg is None)


class IsNotNone:

    def test(self, arg):
        return bool(arg is not None)


class IsEqual:

    def __init__(self, border=0):
        self.border = border

    def test(self, arg):
        return bool(arg == self.border)


class IsGreatThan:

    def __init__(self, border=0):
        self.border = border

    def test(self, arg):
        if any([self.border is None, arg is None]):
            raise TypeError('None is unorderable type')
        return bool(arg > self.border)
