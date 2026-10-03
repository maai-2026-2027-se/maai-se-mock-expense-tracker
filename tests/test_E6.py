import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE6(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.filter_expenses(EXAMPLE, 300, 900), EXAMPLE)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.filter_expenses(EXAMPLE, 300, 300), [EXAMPLE[1]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.filter_expenses([], 0, 1), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        for low, high in [(-1, 5), (5, 4)]:
            with self.subTest(low=low, high=high), self.assertRaises(ValueError):
                app.filter_expenses(EXAMPLE, low, high)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

