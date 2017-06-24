

class Keys:
    km = 'km'
    m = 'm'
    sm = 'sm'


class Unit:
    def __init__(self, label):
        self.label = label


units = {
    Keys.km: Unit(label='Километры'),
    Keys.m: Unit(label='Метры'),
    Keys.sm: Unit(label='Сантиметры')
}
