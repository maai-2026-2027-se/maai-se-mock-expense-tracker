import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestBaseline(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.total_cents([]), 0)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.total_cents(EXAMPLE), 1200)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

