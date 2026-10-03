import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE8(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.summary(EXAMPLE), {'total_cents': 1200, 'categories': {'food': 900, 'travel': 300}, 'people': ['Ada', 'Lin'], 'largest': EXAMPLE[0]})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.summary([]), {'total_cents': 0, 'categories': {}, 'people': [], 'largest': None})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

