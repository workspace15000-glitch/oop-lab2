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


if __name__ == "__main__":
    unittest.main()
