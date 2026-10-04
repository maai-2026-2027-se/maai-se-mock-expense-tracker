import unittest

import app


class TestStudentE5(unittest.TestCase):
    def test_strips_and_casefolds(self):
        self.assertEqual(app.normalize_category("  Cafe  "), "cafe")

    def test_preserves_internal_whitespace(self):
        self.assertEqual(app.normalize_category("Ride  Share"), "ride  share")

    def test_empty_after_strip_raises(self):
        with self.assertRaises(ValueError):
            app.normalize_category("   ")
