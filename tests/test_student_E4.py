import unittest

from app import split_bill


class TestFairSplit(unittest.TestCase):
    def test_multiple_remainder_cents_preserve_total_and_input(self):
        participants = ["Zoe", "Ada", "Lin"]
        shares = split_bill(8, participants)
        self.assertEqual(shares, {"Ada": 3, "Lin": 3, "Zoe": 2})
        self.assertEqual(sum(shares.values()), 8)
        self.assertEqual(participants, ["Zoe", "Ada", "Lin"])

    def test_fewer_cents_than_people(self):
        self.assertEqual(split_bill(1, ["Zoe", "Ada", "Lin"]),
                         {"Ada": 1, "Lin": 0, "Zoe": 0})
