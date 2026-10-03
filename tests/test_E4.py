import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE4(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.split_bill(10, ['C', 'A', 'B']), {'A': 4, 'B': 3, 'C': 3})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.split_bill(0, ['B', 'A']), {'A': 0, 'B': 0})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        for cents, names in [(-1, ['A']), (3, []), (4, ['A', 'A'])]:
            with self.subTest(cents=cents, names=names), self.assertRaises(ValueError):
                app.split_bill(cents, names)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

