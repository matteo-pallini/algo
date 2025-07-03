import unittest

from arrays.exercises.dutch_partitioning import dutch_partitioning, dutch_partitioning_replacement
from arrays.exercises.increment_digits_array import increment_digits_array
from arrays.exercises.advance_array import advance
from arrays.exercises.delete_duplicates import delete_duplicates


class TestDutchPartitioning(unittest.TestCase):

    def test_base_case(self):
        base_test = [3, 1, 0, 1, 10, 6, 2, 5, 4]
        dutch_partitioning_replacement(base_test, 7)
        self.assertEqual(base_test, [1, 0, 1, 2, 3, 4, 5, 6, 10])

    def test_empty_case(self):
        base_test = []
        dutch_partitioning_replacement(base_test, 7)
        self.assertEqual(base_test, [])

    def test_all_equal(self):
        base_test = [4, 4, 4, 4]
        dutch_partitioning_replacement(base_test, 2)
        self.assertEqual(base_test, [4, 4, 4, 4])

    def test_single_value(self):
        base_test = [1]
        dutch_partitioning_replacement(base_test, 0)
        self.assertEqual(base_test, [1])


class TestIncrementDigitArray(unittest.TestCase):

    def test_base_case(self):
        base_case = [1, 0, 0]
        expected = [1, 0, 1]
        self.assertEqual(increment_digits_array(base_case), expected)

    def test_case_with_nines(self):
        base_case = [1, 9, 9]
        expected = [2, 0, 0]
        self.assertEqual(increment_digits_array(base_case), expected)

    def test_overflowing_case(self):
        base_case = [9, 9, 9]
        expected = [1, 0, 0, 0]
        self.assertEqual(increment_digits_array(base_case), expected)


class TestAdvanceArray(unittest.TestCase):

    def test_valid_case(self):
        valid_array = [3, 3, 1, 0, 2, 0, 1]
        expected = True
        actual = advance(valid_array, 0, 0)
        self.assertEqual(actual, expected)

    def test_invalid_case(self):
        invalid_array = [3, 3, 1, 0, 0, 0, 2, 0, 1]
        expected = False
        actual = advance(invalid_array, 0, 0)
        self.assertEqual(actual, expected)

    def test_empty_array(self):
        empty_array = []
        expected = True
        actual = advance(empty_array, 0, 0)
        self.assertEqual(actual, expected)


class TestDeleteDuplicates(unittest.TestCase):

    def test_delete_duplicates(self):
        arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
        actual = delete_duplicates(arr)
        expected = [2, 3, 5, 7, 11, 13]
        self.assertEqual(expected, actual)

    def test_no_duplicates_to_delete(self):
        arr = [2, 3, 5, 7, 11, 13]
        actual = delete_duplicates(arr)
        expected = [2, 3, 5, 7, 11, 13]
        self.assertEqual(expected, actual)
