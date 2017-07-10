import unittest

from examples.methods_chain.dsl_board.semantic_model.board import Board
from examples.methods_chain.dsl_board.semantic_model.card import Card
from examples.methods_chain.dsl_board.semantic_model.cut import Cut
from examples.methods_chain.dsl_board.semantic_model.swimlane import SwimLane


class TestBoardSerializeDeserialize(unittest.TestCase):
    board = Board('Story Map', [
        Cut('ReleaseA', [
            SwimLane('Todo', [
                Card('Too many code, to many concepts.'),
                Card('Cats is cuts with nuts.')
            ])
        ])
    ])

    def test__to_dict__from_dict(self):
        expected = self.board

        dict_ = self.board.to_dict()
        result = Board.from_dict(dict_)

        self.assertEqual(expected, result)

    def test__to_json_file__from_json_file(self):
        path = 'ng_django/examples/dsl_board/board.json'
        expected = self.board

        expected.to_json_file(path)
        result = Board.from_json_file(path)

        self.assertEqual(expected, result)

    def test__to_json__from_json(self):
        expected = self.board

        result = Board.from_json(expected.to_json())

        self.assertEqual(expected, result)
