import copy
import unittest

import app


class TestStudentE2(unittest.TestCase):

    def test_people_removes_duplicates_and_sorts(self):
        expenses = [
            {"person": "Zoe", "category": "food", "cents": 500},
            {"person": "Amy", "category": "travel", "cents": 200},
            {"person": "Zoe", "category": "books", "cents": 300},
        ]
        original = copy.deepcopy(expenses)

        self.assertEqual(app.people(expenses), ["Amy", "Zoe"])
        self.assertEqual(expenses, original)

    def test_people_empty_input(self):
        self.assertEqual(app.people([]), [])


if __name__ == "__main__":
    unittest.main()