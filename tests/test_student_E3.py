import unittest
from copy import deepcopy

from app import largest_expense


class TestStudentE3(unittest.TestCase):
    def test_largest_without_changing_input(self):
        expenses = [
            {"person": "A", "category": "food", "cents": 100},
            {"person": "B", "category": "travel", "cents": 900},
            {"person": "C", "category": "food", "cents": 300},
        ]
        original = deepcopy(expenses)

        self.assertEqual(largest_expense(expenses), expenses[1])
        self.assertEqual(expenses, original)

    def test_first_record_wins_tie(self):
        first = {"person": "A", "category": "food", "cents": 500}
        second = {"person": "B", "category": "travel", "cents": 500}

        self.assertEqual(largest_expense([first, second]), first)

    def test_empty_input(self):
        self.assertIsNone(largest_expense([]))