import json
from collections import namedtuple

path = 'examples/symbols_table/test_4/units.json'

Field = namedtuple('Field', ['label'])


class Unit:

    @staticmethod
    def create_from_json(path):
        with open(path, 'r') as file:
            dict_ = json.load(file)
        return Unit(dict_)

    def __init__(self, dict_):
        self.fields = {k: Field(label=v) for k, v in dict_.items()}

    def __getattr__(self, key):
        return self.fields.get(key)

    def __getitem__(self, key):
        return self.fields.get(key)


units = Unit.create_from_json(path)
