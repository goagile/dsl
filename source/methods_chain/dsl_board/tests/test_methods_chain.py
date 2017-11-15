import unittest

from examples.methods_chain.dsl_board.semantic_model.board import Board
from examples.methods_chain.dsl_board.semantic_model.card import Card
from examples.methods_chain.dsl_board.semantic_model.cut import Cut
from examples.methods_chain.dsl_board.semantic_model.swimlane import SwimLane

from examples.methods_chain.dsl_board.methods_chain.model import board, cut


class TestMethodChainingCreation(unittest.TestCase):
    board = Board('Story Map', [
        Cut('ReleaseA', [
            SwimLane('Todo', [
                Card('Too many code, to many concepts.'),
                Card('Cats is cuts with nuts.')
            ])
        ])
    ])

    @unittest.skip('')
    def test(self):
        expected = self.board

        result = \
            board('Story Map', (
                cut('ReleaseA')
                    .swimlane('Todo')
                        .card('Too many code, to many concepts.')
                        .card('Cats is cuts with nuts.')
            ))

        self.assertEqual(expected, result)
