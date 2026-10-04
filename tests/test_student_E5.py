import unittest
import app


class TestStudentE5(unittest.TestCase):
    def test_normalizes_and_preserves_internal_whitespace(self):
        self.assertEqual(
            app.normalize_category(" \tStraße  TAX\tOffice\n"),
            "strasse  tax\toffice",
        )

    def test_rejects_empty_categories(self):
        for label in ("", " \t\n "):
            with self.subTest(label=label):
                with self.assertRaises(ValueError):
                    app.normalize_category(label)
