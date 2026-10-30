import unittest

from regex_checker import FloatValidator


class TestFloatValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = FloatValidator()

    def test_valid_numbers(self) -> None:
        values = [
            "3.14", "-0.5", "+12.75", ".5", "-.25", "5.", "0.0",
            "1e3", "-2E-4", "+6.02e+23", ".5e2", "5.e-1",
        ]
        for value in values:
            with self.subTest(value=value):
                self.assertTrue(self.validator.is_valid(value))

    def test_invalid_numbers(self) -> None:
        values = [
            "", "42", "-7", ".", "+.", "1,5", "1.2.3", "1e", "1.5e+",
            "--2.5", "abc", "NaN", "inf", "2.5ms", " 3.14", "3.14\n",
        ]
        for value in values:
            with self.subTest(value=value):
                self.assertFalse(self.validator.is_valid(value))

    def test_search_in_text(self) -> None:
        text = "Числа: -3.14; +0.5, .25 и 2e-3."
        self.assertEqual(
            self.validator.validate_text(text),
            ["-3.14", "+0.5", ".25", "2e-3"],
        )

    def test_search_skips_invalid_fragments(self) -> None:
        text = "v1.2.3 abc1.5 2.5ms 1.5e+ --2.5 42 1,5"
        self.assertEqual(self.validator.validate_text(text), [])

    def test_search_keeps_repeated_numbers(self) -> None:
        self.assertEqual(self.validator.validate_text("1.5 1.5"), ["1.5", "1.5"])

    def test_search_empty_text(self) -> None:
        self.assertEqual(self.validator.validate_text(""), [])


if __name__ == "__main__":
    unittest.main()
