import json

from dsl_board.semantic_model.base import CompositeBoardElement
from dsl_board.semantic_model.cut import Cut


class Board(CompositeBoardElement):
    row_class = Cut

    def is_empty(self):
        return bool(not self.rows)

    def to_json_file(self, path):
        dict_ = self.to_dict()
        with open(path, 'w') as file:
            json.dump(dict_, file, ensure_ascii=True, indent=True)

    @classmethod
    def from_json_file(cls, path):
        dict_ = {}
        with open(path, 'r') as file:
            dict_ = json.load(file)
        return cls.from_dict(dict_)

    def to_json(self):
        dict_ = self.to_dict()
        result = json.dumps(dict_, ensure_ascii=True, indent=True)
        return result

    @classmethod
    def from_json(cls, json_):
        dict_ = json.loads(json_)
        result = cls.from_dict(dict_)
        return result
