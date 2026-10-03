import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE3(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertIsNone(app.largest_expense([]))
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.largest_expense(EXAMPLE), EXAMPLE[0])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        a = dict(person='A', category='x', cents=4)
        b = dict(person='B', category='x', cents=4)
        self.assertEqual(app.largest_expense([a, b]), a)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

