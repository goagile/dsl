import re
import unittest

from examples.methods_chain.dsl_board.semantic_model.board import Board


class Test(unittest.TestCase):

    def test(self):
        # expected = Board(name='Интернет магазин', rows=[])
        expected = Board(name='TEST', rows=[])
        text = """
[board]
name = Интернет магазин
        """

        result = BoardIniParser().parse(text)

        self.assertEqual(expected, result)


class BoardIniParser:

    def __init__(self):
        self.board = None

    def parse(self, text):
        lines = text.split('\n')
        lines = [line for line in lines if line.strip()]
        for line in lines:
            if self.is_section(line):
                self.parse_section(line)
            elif self.is_property(line):
                self.parse_property(line)
        return self.board

    def is_section(self, line):
        if re.match(r'^\s*\[', line):
            return True
        return False

    def parse_section(self, line):
        section_name = re.search(r'^\s*\[(.*)\]', line).groups(0)[0]
        if section_name == 'board':
            self.board = Board(name='TEST', rows=[])
            return
        raise ValueError('Section not found')

    def is_property(self, line):
        if re.match(r'(.*)=(.*)', line):
            return True
        return False

    def parse_property(self,line):
        name = line.split('=')[0].strip()
        value = line.split('=')[1].strip()
        if name == 'name':
            self.board.name = value
            return
        raise ValueError('Property not found')
