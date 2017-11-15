from collections import namedtuple


class Keys:
    km = 'km'
    m = 'm'
    sm = 'sm'


Units = namedtuple('Units', [
    Keys.km,
    Keys.m,
    Keys.sm
])


class Unit:
    def __init__(self, label):
        self.label = label


units = Units(
    km=Unit(label='Километры'),
    m=Unit(label='Метры'),
    sm=Unit(label='Сантиметры')
)
