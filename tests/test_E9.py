import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'person': 'Ada', 'category': 'food', 'cents': 900}, {'person': 'Lin', 'category': 'travel', 'cents': 300}]


class TestE9(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv([]), 'person,category,cents\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv(EXAMPLE), 'person,category,cents\nAda,food,900\nLin,travel,300\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(person='A, B', category='A\"B\nC', cents=5)]
        self.assertEqual(list(csv.reader(io.StringIO(app.to_csv(rows)))), [['person', 'category', 'cents'], ['A, B', 'A\"B\nC', '5']])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

