import copy
import unittest

import app


class TestStudentE8(unittest.TestCase):
    def test_summary_combines_repeated_categories_and_people(self):
        expenses = [
            {"person": "Zoe", "category": "food", "cents": 200},
            {"person": "Amy", "category": "food", "cents": 500},
            {"person": "Zoe", "category": "travel", "cents": 100},
        ]
        original = copy.deepcopy(expenses)

        self.assertEqual(app.summary(expenses), {
            "total_cents": 800,
            "categories": {"food": 700, "travel": 100},
            "people": ["Amy", "Zoe"],
            "largest": original[1],
        })
        self.assertEqual(expenses, original)

    def test_empty_summary(self):
        self.assertEqual(app.summary([]), {
            "total_cents": 0,
            "categories": {},
            "people": [],
            "largest": None,
        })
