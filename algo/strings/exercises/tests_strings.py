import unittest
from strings.exercises.convert_without_using_int import string_to_int, int_to_string
from strings.exercises.spreadsheet_column_checking import spreadsheet_column_checking
from strings.exercises.palindromicity import palindromicity
from strings.exercises.phone_mnemonics import phone_mnemonics
from strings.exercises.roman_to_decimal import roman_to_decimal
from strings.exercises.string_sinusoidally import string_sinusoidally
from strings.exercises.interconvert_str_and_int import intercovert


class TestCase(unittest.TestCase):

    def test_positive_string_to_int(self):
        value = "184"
        actual = string_to_int(value)
        expected = 184
        self.assertEqual(actual, expected)

    def test_negative_string_to_int(self):
        value = "-18542"
        actual = string_to_int(value)
        expected = -18542
        self.assertEqual(actual, expected)

    def test_positive_int_to_string(self):
        value = 184
        actual = int_to_string(value)
        expected = "184"
        self.assertEqual(actual, expected)

    def test_negative_int_to_string(self):
        value = -18542
        actual = int_to_string(value)
        expected = "-18542"
        self.assertEqual(actual, expected)


class TestSpreadsheetColumnChecking(unittest.TestCase):

    def test_one_elem(self):
        value = "E"
        expected = 5
        actual = spreadsheet_column_checking(value)
        self.assertEqual(expected, actual)

    def test_one_elem_boundary(self):
        value = "A"
        expected = 1
        actual = spreadsheet_column_checking(value)
        self.assertEqual(expected, actual)

    def test_two_elems_boundary(self):
        value = "AA"
        expected = 27
        actual = spreadsheet_column_checking(value)
        self.assertEqual(expected, actual)

    def test_two_elems(self):
        value = "DE"
        expected = 26 * 4 + 5
        actual = spreadsheet_column_checking(value)
        self.assertEqual(expected, actual)

    def test_three_elems(self):
        value = "ZZ"
        expected = 702
        actual = spreadsheet_column_checking(value)
        self.assertEqual(expected, actual)


class TestPalindromicity(unittest.TestCase):

    def test_base_case(self):
        base_case = "oppo!"
        actual = palindromicity(base_case)
        self.assertTrue(actual)

    def test_book_case_one(self):
        base_case = "A man, a plan, a canal, Panama."
        actual = palindromicity(base_case)
        self.assertTrue(actual)

    def test_book_case_two(self):
        base_case = "Able was I, ere I saw Elba!"
        actual = palindromicity(base_case)
        self.assertTrue(actual)

    def test_book_case_three(self):
        base_case = "Ray a Ray"
        actual = palindromicity(base_case)
        self.assertFalse(actual)


class TestPhoneMnemonics(unittest.TestCase):

    def test_base_case(self):
        value = "234"
        expected = [
            "adg", "adh", "adi",
            "aeg", "aeh", "aei",
            "afg", "afh", "afi",
            "bdg", "bdh", "bdi",
            "beg", "beh", "bei",
            "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi",
            "ceg", "ceh", "cei",
            "cfg", "cfh", "cfi",
        ]
        actual = phone_mnemonics(value)
        self.assertListEqual(expected, actual)


class TestRomanToDecimal(unittest.TestCase):

    def test_base_case_single(self):
        value = "X"
        expected = 10
        actual = roman_to_decimal(value)
        self.assertEqual(actual, expected)

    def test_base_case_double(self):
        value = "XX"
        expected = 20
        actual = roman_to_decimal(value)
        self.assertEqual(actual, expected)

    def test_base_case_double_minus(self):
        value = "IX"
        expected = 9
        actual = roman_to_decimal(value)
        self.assertEqual(actual, expected)

    def test_base_case_triple(self):
        value = "LIX"
        expected = 59
        actual = roman_to_decimal(value)
        self.assertEqual(actual, expected)


class TestStringSinusoidally(unittest.TestCase):

    def test_base_case(self):
        value = "Hello World!"
        expected = "e lHloWrdlo!"
        actual = string_sinusoidally(value)
        self.assertEqual(actual, expected)


class TestInterconvertStrAndInt(unittest.TestCase):

    def test_base_case_string(self):
        expected = 3249
        self.assertEqual(intercovert(str(expected)), expected)

    def test_base_case_int(self):
        expected = "3249"
        self.assertEqual(intercovert(int(expected)), expected)

    def test_base_case_string_neg(self):
        expected = "-3249"
        self.assertEqual(intercovert(-3249), expected)

    def test_base_case_int_neg(self):
        expected = -3249
        self.assertEqual(intercovert("-3249"), expected)
