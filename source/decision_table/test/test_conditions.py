import unittest
from test.fixtures import pznt
from custom.conditions import (
    IsNone,
    IsNotNone,
    IsEqual,
    IsGreatThan,
)
from core.result import Result
from core.row import Row
from core.table import DecisionTable


class TestAcceptance(unittest.TestCase):

    @unittest.skip('json is not realized')
    def test_analize_json_and_compile_settings(self):
        table = JSONTableAnalizer(pznt['from_file']).analize()
        settings = table.compile_settings(pznt['case_1']['parsed_settings'])
        self.assertEqual(pznt['case_1']['to_bf'], settings)


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = DecisionTable()

    def tearDown(self):
        self.table = None

    def test_table_calc_results(self):
        self.table.rows = [
            Row([IsNotNone(), IsGreatThan(0)], [Result(2),  Result(0)]),
            Row([IsNone(),    IsEqual(0)],     [Result(10), Result(1)]),
        ]
        self.assertEqual(self.table.calc([3,    2]), [2,  0])
        self.assertEqual(self.table.calc([None, 0]), [10, 1])

    def test_table_get_results(self):
        self.table.rows = [
            Row([IsNotNone(), IsGreatThan(0)], [Result(2),  Result(0)]),
            Row([IsNone(),    IsEqual(0)],     [Result(10), Result(1)]),
        ]
        self.assertEqual(self.table.get_results([3,    2]), [Result(2),  Result(0)])
        self.assertEqual(self.table.get_results([None, 0]), [Result(10), Result(1)])

    def test_no_one_rows_has_true_test(self):
        self.table.rows = [
            Row([IsNone(), IsEqual(0)], []),
        ]
        with self.assertRaises(ValueError):
            self.table.get_results([None, 56])

    def test_raises_empty_rows_list(self):
        self.table.rows = []
        with self.assertRaises(ValueError):
            self.table.get_results([3, 2])


class TestRows(unittest.TestCase):

    def test_Row_test(self):
        row = Row([IsNotNone(), IsGreatThan(0)], [])
        self.assertTrue(row.test([2,     1]))
        self.assertFalse(row.test([2,   -1]))
        self.assertFalse(row.test([None, 1]))
        self.assertFalse(row.test([None, 0]))


class TestConditions(unittest.TestCase):

    def test_IsNone(self):
        self.assertTrue(IsNone().test(None))
        self.assertFalse(IsNone().test('3.0'))
        self.assertFalse(IsNone().test(2.0))
        self.assertFalse(IsNone().test(1))

    def test_IsNotNone(self):
        self.assertTrue(IsNotNone().test(1))
        self.assertTrue(IsNotNone().test(2.0))
        self.assertTrue(IsNotNone().test('3.0'))
        self.assertFalse(IsNotNone().test(None))

    def test_IsEqual(self):
        self.assertTrue(IsEqual(1).test(1))
        self.assertTrue(IsEqual(2.0).test(2.0))
        self.assertTrue(IsEqual('3.0').test('3.0'))
        self.assertTrue(IsEqual(None).test(None))
        self.assertTrue(IsEqual(2).test(2.0))
        self.assertFalse(IsEqual(1).test(2))
        self.assertFalse(IsEqual(3).test('3.0'))
        self.assertFalse(IsEqual(1).test(None))

    def test_IsGreatThan_0(self):
        self.assertTrue(IsGreatThan(0).test(1))
        self.assertTrue(IsGreatThan(0).test(2.0))
        self.assertFalse(IsGreatThan(0).test(0))
        self.assertFalse(IsGreatThan(0).test(-1))
        with self.assertRaises(TypeError):
            IsGreatThan(0).test(None)
