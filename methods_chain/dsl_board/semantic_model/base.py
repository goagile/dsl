from dsl_board.registry.registry import register_class, from_registry

from dsl_board.serializers.serializers import CompositeBoardElementSerializer, BoardElementSerializer


class BoardElementMeta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls


class BoardElement(metaclass=BoardElementMeta):

    def __init__(self, name):
        self.name = name
        self.serializer = BoardElementSerializer(self)

    def __eq__(self, other):
        return bool(self.name == other.name)

    def to_dict(self):
        result = {
            'name': self.name
        }
        return result

    @classmethod
    def from_dict(cls, dict_):
        klass = from_registry(cls.__name__)
        name = dict_.get('name', '')
        result = klass(name)
        return result


class CompositeBoardElement(BoardElement):

    def __init__(self, name, rows):
        super().__init__(name)
        self.rows = rows
        self.serializer = CompositeBoardElementSerializer(self)

    def __eq__(self, other):
        return all([
            self.name == other.name,
            all(s == o for s, o in zip(self.rows, other.rows))
        ])

    @classmethod
    def from_dict(cls, dict_):
        klass = from_registry(cls.__name__)
        name = dict_.get('name', '')
        rows = [
            klass.row_class.from_dict(row) for row in dict_.get('rows', [])
        ]
        result = klass(name, rows)
        return result
