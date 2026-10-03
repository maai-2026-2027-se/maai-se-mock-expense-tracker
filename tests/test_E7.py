import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE7(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.balances(EXAMPLE, ['Ada', 'Lin', 'Sam']), {'Ada': 500, 'Lin': -100, 'Sam': -400})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.balances([], ['A', 'B']), {'A': 0, 'B': 0})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.balances([dict(person='B', category='x', cents=1)], ['A', 'B']), {'A': -1, 'B': 1})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(ValueError):
            app.balances(EXAMPLE, ['Ada'])
        with self.assertRaises(ValueError):
            app.balances([], [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

