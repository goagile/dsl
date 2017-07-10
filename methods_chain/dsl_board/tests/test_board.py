import unittest

from examples.methods_chain.dsl_board.semantic_model.board import Board


class TestBoard(unittest.TestCase):

    def test_board_is_empty(self):
        board = Board('', None)

        result = board.is_empty()

        self.assertTrue(result)

    def test_board_is_not_empty__with_one_cut(self):
        board = Board('', [1])

        result = board.is_empty()

        self.assertFalse(result)
