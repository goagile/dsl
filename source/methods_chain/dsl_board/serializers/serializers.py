from examples.methods_chain.dsl_board.registry.registry import from_registry


class BoardElementSerializer:

    def __init__(self, board_element):
        self.board_element = board_element

    def to_dict(self):
        result = {
            'name': self.board_element.name
        }
        return result

    @classmethod
    def from_dict(cls, dict_):
        name = dict_.get('name', '')
        klass = from_registry(cls.__name__)
        instance = klass(name)
        return instance


class CompositeBoardElementSerializer:

    def __init__(self, board_element):
        self.board_element = board_element

    def to_dict(self):
        result = {
            'name': self.board_element.name,
            'rows': [row.to_dict() for row in self.board_element.rows]
        }
        return result

    @classmethod
    def from_dict(cls, dict_):
        name = dict_.get('name', '')
        klass = from_registry(cls.__name__)
        rows = [
            cls.row_class.from_dict(row) for row in dict_.get('rows', [])
        ]
        instance = klass(name, rows)
        return instance
