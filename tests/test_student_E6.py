import copy
import unittest

import app


class TestStudentE6(unittest.TestCase):
    def test_inclusive_bounds_keep_endpoints(self):
        expenses = [
            {"person": "Ada", "category": "food", "cents": 100},
            {"person": "Lin", "category": "travel", "cents": 200},
            {"person": "Zoe", "category": "books", "cents": 300},
        ]
        original = copy.deepcopy(expenses)
        self.assertEqual(
            app.filter_expenses(expenses, 100, 200),
            expenses[:2],
        )
        self.assertEqual(expenses, original)

    def test_negative_minimum_raises(self):
        with self.assertRaises(ValueError):
            app.filter_expenses([], -1, 10)
